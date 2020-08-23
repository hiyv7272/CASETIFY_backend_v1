import json
import requests

from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.mail.message import EmailMessage
from user.utils import login_decorator
from my_settings import SMS_AUTH_ID, SMS_SERVICE_SECRET, SMS_FROM_NUMBER, SMS_URL

from .models import Order, CheckoutStatus, Cart
from user.models import User


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
            Cart.objects.create(
                USER_id=request.user.id,
                ARTWORK_id=data['ARTWORK_id'],
                ARTWORK_PRICE_id=data['ARTWORK_PRICE_id'],
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
        ).filter(USER=request.user.id, is_custom=True).order_by('id')

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
        ).filter(USER=request.user.id, is_custom=False).order_by('id')

        try:
            custom_cart_list = list()
            regular_cart_list = list()

            for result in custom_cart:
                dict_data = dict()
                dict_data['id'] = result.id
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
                dict_data['id'] = result.id
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
        data = json.loads(request.body)
        user = User.objects.get(id=request.user.id)

        try:
            user.mobile_number = data['mobile_number']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.address = data['address']
            user.zipcode = data['zipcode']
            user.save()

            for cart_id in data['id']:

                Cart.objects.filter(id=cart_id).update(is_checkout=True)
                Order(
                    CART=Cart.objects.get(id=cart_id),
                    USER=user,
                    CHECKOUT_STATUS=CheckoutStatus.objects.get(id=3)
                ).save()

            # email(data, user)
            # self.sms_service(data, user)
            return HttpResponse(status=200)

        except Order.DoesNotExist:
            return JsonResponse({"message": "INVALID_VALUE"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)

    @login_decorator
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        order = Order.objects.select_related(
            'CART',
            'USER',
            'ORDER_STATUS'
        ).filter(USER=request.user.id, ORDER_STATUS=3).order_by('id')

        cart = Cart.objects.select_related(
            'USER',
            'ARTWORK',
            'ARTWORK_COLOR',
            'ARTWORK_PRICE'
        ).filter(USER=request.user.id, is_checkout=True)

        try:
            orders = list()
            user_data = dict()

            user_data['email'] = user.email
            user_data['mobile_number'] = user.mobile_number
            user_data['first_name'] = user.first_name
            user_data['last_name'] = user.last_name
            user_data['address'] = user.address
            user_data['zipcode'] = user.zipcode

            for order_row in order:
                dict_data = dict()
                dict_data['cart_id'] = order_row.CART.id
                dict_data['user'] = order_row.USER.name
                dict_data['order_status'] = order_row.ORDER_STATUS.name

                for cart_row in cart:
                    if cart_row.id == dict_data['cart_id']:
                        dict_data['artwork'] = cart_row.ARTWORK.name
                        dict_data['artwork_color'] = cart_row.ARTWORK_COLOR.name
                        dict_data['artwork_price'] = cart_row.ARTWORK_PRICE.price
                        dict_data['is_customed'] = cart_row.is_customed
                        dict_data['custom_info'] = cart_row.custom_info

                orders.append(dict_data)

            return JsonResponse({
                "user_data": user_data,
                "orders": orders,
            }, status=200)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)


