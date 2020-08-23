import json
import requests

from datetime import datetime
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.mail.message import EmailMessage
from django.db import transaction
from user.utils import login_decorator
from my_settings import SMS_AUTH_ID, SMS_SERVICE_SECRET, SMS_FROM_NUMBER, SMS_URL

from .models import Order, Orderer, CheckoutStatus, CheckOut, Cart
from user.models import User
from artwork.models import ArtworkPrice


def email(data, user):
    for id in data['id']:
        info = Order.objects.select_related('USER', 'ARTWORK').get(id=id)
    if len(data['id']) > 1:
        subject = 'CASETIFY-PROJECT'
        message = f"""{user.last_name}{user.first_name}님 {info.ARTWORK.name}외 상품 결제완료되었습니다. \n감사합니다 :)"""
        email = EmailMessage(subject=subject, body=message, to=[user.email])
    else:
        subject = 'CASETIFY-PROJECT'
        message = f"""{user.last_name}{user.first_name}님 {info.ARTWORK.name}상품 결제완료되었습니다. \n감사합니다 :)"""
        email = EmailMessage(subject=subject, body=message, to=[user.email])
    email.send()


def sms_service(data, user):
    for id in data['id']:
        info = Order.objects.select_related('USER', 'ARTWORK').get(id=id)
    mobile_number = info.user.mobile_number

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'x-ncp-auth-key': f'{SMS_AUTH_ID}',
        'x-ncp-service-secret': f'{SMS_SERVICE_SECRET}',
    }

    data = {
        'type': 'SMS',
        'contentType': 'COMM',
        'countryCode': '82',
        'from': f"""{SMS_FROM_NUMBER}""",
        'to': [f"""{mobile_number}"""],
        'subject': 'CASETIFY-PROJECT',
        'content': f"""{user.last_name}{user.first_name}님! {info.artwork.name}상품 결제가 완료되었습니다. \n감사합니다 :)"""
    }
    requests.post(SMS_URL, headers=headers, json=data)


class CartView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)

        try:
            artwork_price = ArtworkPrice.objects.all()
            Cart.objects.create(
                USER_id=request.user.id,
                ARTWORK_id=data['ARTWORK_id'],
                ARTWORK_PRICE_id=artwork_price.get(ARTWORK=data['ARTWORK_id']).id,
                is_custom=data['is_custom'],
                custom_info=data['custom_info'],
                quantity=data['quantity'],
                is_use=True
            )

            return HttpResponse(status=200)

        except Cart.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)

    @login_decorator
    def get(self, request):
        custom_cart = Cart.objects.select_related(
            'USER',
            'ARTWORK',
            'ARTWORK_PRICE'
        ).select_related(
            'ARTWORK__FEATURED',
            'ARTWORK__DEVICE',
            'ARTWORK__ARTWORK_COLOR',
            'ARTWORK__ARTWORK_TYPE',
            'ARTWORK__ARTIST'
        ).filter(USER=request.user.id, is_custom=True, is_use=True).order_by('id')

        regular_cart = Cart.objects.select_related(
            'USER',
            'ARTWORK',
            'ARTWORK_PRICE'
        ).select_related(
            'ARTWORK__FEATURED',
            'ARTWORK__DEVICE',
            'ARTWORK__ARTWORK_COLOR',
            'ARTWORK__ARTWORK_TYPE',
            'ARTWORK__ARTIST'
        ).filter(USER=request.user.id, is_custom=False, is_use=True).order_by('id')

        try:
            custom_cart_list = list()
            regular_cart_list = list()

            for result in custom_cart:
                dict_data = dict()
                dict_data['cart_id'] = result.id
                dict_data['artwork_id'] = result.ARTWORK.id
                dict_data['artwork_name'] = result.ARTWORK.name
                dict_data['artwork_device_name'] = result.ARTWORK.DEVICE.name
                dict_data['artwork_color_name'] = result.ARTWORK.ARTWORK_COLOR.name
                dict_data['artwork_type'] = result.ARTWORK.ARTWORK_TYPE.name
                dict_data['artwork_price'] = result.ARTWORK_PRICE.price
                dict_data['artwork_artist_name'] = result.ARTWORK.ARTIST.name
                dict_data['is_custom'] = result.is_custom
                dict_data['custom_info'] = result.custom_info
                dict_data['quantity'] = result.quantity

                custom_cart_list.append(dict_data)

            for result in regular_cart:
                dict_data = dict()
                dict_data['cart_id'] = result.id
                dict_data['artwork_id'] = result.ARTWORK.id
                dict_data['artwork_name'] = result.ARTWORK.name
                dict_data['artwork_device_name'] = result.ARTWORK.DEVICE.name
                dict_data['artwork_color_name'] = result.ARTWORK.ARTWORK_COLOR.name
                dict_data['artwork_type'] = result.ARTWORK.ARTWORK_TYPE.name
                dict_data['artwork_price'] = result.ARTWORK_PRICE.price
                dict_data['artwork_artist_name'] = result.ARTWORK.ARTIST.name
                dict_data['is_custom'] = result.is_custom
                dict_data['custom_info'] = result.custom_info
                dict_data['quantity'] = result.quantity

                regular_cart_list.append(dict_data)

            return JsonResponse({
                "custom_orders": custom_cart_list,
                "regular_orders": regular_cart_list
            }, status=200)

        except Cart.DoesNotExist:
            return JsonResponse({"message": "INVALID_VALUE"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)


class OrderView(View):
    @login_decorator
    def post(self, request):
        with transaction.atomic():

            try:
                delivery_price = float("5.99")
                sub_total_price = float("00.00")
                order_number = datetime.now().strftime('%Y%m%d%H%m%s')
                user_id = request.user.id

                print(request.GET.get('first_name'))
                Orderer(
                    USER=User.objects.get(id=user_id),
                    first_name=request.GET.get('first_name'),
                    last_name=request.GET.get('last_name'),
                    address=request.GET.get('address'),
                    zipcode=request.GET.get('zipcode'),
                    mobile_number=request.GET.get('mobile_number')
                ).save()

                for cart_id in request.GET.get('cart_id').split(','):
                    cart = Cart.objects.get(id=cart_id)
                    cart.is_use = False
                    cart.save()
                    sub_total_price += float(Cart.objects.select_related('ARTWORK_PRICE').get(id=cart_id).ARTWORK_PRICE.price)

                if sub_total_price > 49.00:
                    delivery_price = float("00.00")

                total_price = sub_total_price + delivery_price
                print(Orderer.objects.get(USER=request.user.id))
                Order(
                    USER=User.objects.get(id=user_id),
                    ORDERER=Orderer.objects.get(USER=request.user.id),
                    order_number=order_number,
                    delivery_price=delivery_price,
                    sub_total_price=sub_total_price,
                    total_price=total_price,
                    is_use=True
                ).save()

                for cart_id in request.GET.get('cart_id').split(','):
                    CheckOut(
                        USER=User.objects.get(id=user_id),
                        CART=Cart.objects.get(id=cart_id),
                        ORDER=Order.objects.get(order_number=order_number),
                        CHECKOUT_STATUS=CheckoutStatus.objects.get(name='결제완료'),
                        custom_info=Cart.objects.get(id=cart_id).custom_info,
                        quantity=Cart.objects.get(id=cart_id).quantity,
                        sell_price=Cart.objects.select_related('ARTWORK_PRICE').get(id=cart_id).ARTWORK_PRICE.price,
                        is_use=True
                    ).save()

                return HttpResponse(status=200)
            except KeyError:
                return JsonResponse({'message': 'INVALID_KEYS'}, status=400)

    @login_decorator
    def get(self, request):

        try:
            order_list = list()

            order = Order.objects.select_related(
                'USER',
                'ORDERER'
            ).all().filter(USER=request.user.id)

            for row in order:
                dict_data = dict()
                dict_data['order_id'] = row.id
                dict_data['order_number'] = row.order_number
                dict_data['delivery_price'] = row.delivery_price
                dict_data['sub_total_price'] = row.sub_total_price
                dict_data['total_price'] = row.total_price
                dict_data['order_datetime'] = row.create_datetime
                dict_data['orderer_name'] = row.ORDERER.last_name + row.ORDERER.first_name
                dict_data['orderer_address'] = row.ORDERER.address
                dict_data['orderer_zipcode'] = row.ORDERER.zipcode

                order_list.append(dict_data)

            return JsonResponse({"data": order_list}, status=200)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)


class OrderDetailView(View):
    @login_decorator
    def get(self, request):
        try:
            order_id = request.GET.get('order_id')
            checkout = CheckOut.objects.select_related(
                'ORDER',
                'CHECKOUT_STATUS'
            ).filter(ORDER=order_id)

            checkout_list = list()

            for row in checkout:
                dict_data = dict()
                dict_data['checkout_id'] = row.id
                dict_data['checkout_status'] = row.CHECKOUT_STATUS.name
                dict_data['custom_info'] = row.custom_info
                dict_data['quantity'] = row.quantity
                dict_data['sell_price'] = row.sell_price
                dict_data['checkout_datetime'] = row.create_datetime

                checkout_list.append(dict_data)

            return JsonResponse({"data": checkout_list}, status=200)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)
