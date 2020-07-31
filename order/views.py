import json
import requests

from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.mail.message import EmailMessage
from user.utils import login_decorator
from my_settings import SMS_AUTH_ID, SMS_SERVICE_SECRET, SMS_FROM_NUMBER, SMS_URL

from .models import Order, Cart
from user.models import User


def email(data, user):
    for id in data['id']:
        info = Order.objects.select_related('user', 'artwork').get(id=id)
    if len(data['id']) > 1:
        subject = 'CASETIFY-PROJECT'
        message = f"""{user.last_name}{user.first_name}님 {info.artwork.name}외 상품 결제완료되었습니다. \n감사합니다 :)"""
        email = EmailMessage(subject=subject, body=message, to=[user.email])
    else:
        subject = 'CASETIFY-PROJECT'
        message = f"""{user.last_name}{user.first_name}님 {info.artwork.name}상품 결제완료되었습니다. \n감사합니다 :)"""
        email = EmailMessage(subject=subject, body=message, to=[user.email])
    email.send()


def sms_service(data, user):
    for id in data['id']:
        info = Order.objects.select_related('user', 'artwork').get(id=id)
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
                ARTWORK_id=data['artwork_id'],
                ARTWORK_COLOR_id=data['artwork_color_id'],
                ARTWORK_PRICE_id=data['artwork_price_id'],
                is_customed=data['is_customed']
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
            'ARTWORK_COLOR',
            'ARTWORK_PRICE'
        ).filter(USER=request.user.id, is_customed=True).order_by('id')

        regular_cart = Cart.objects.select_related(
            'USER',
            'ARTWORK',
            'ARTWORK_COLOR',
            'ARTWORK_PRICE'
        ).filter(USER=request.user.id, is_customed=False).order_by('id')

        try:
            custom_cart_list = list()
            regular_cart_list = list()

            for result in custom_cart:
                dict_data = dict()
                dict_data['id'] = result.id
                dict_data['user'] = result.USER.name
                dict_data['artwork'] = result.ARTWORK.name
                dict_data['artwork_color'] = result.ARTWORK_COLOR.name
                dict_data['artwork_price'] = result.ARTWORK_PRICE.price
                dict_data['is_customed'] = result.is_customed
                dict_data['custom_info'] = result.custom_info

                custom_cart_list.append(dict_data)

            for result in regular_cart:
                dict_data = dict()
                dict_data['id'] = result.id
                dict_data['user'] = result.USER.name
                dict_data['artwork'] = result.ARTWORK.name
                dict_data['artwork_color'] = result.ARTWORK_COLOR.name
                dict_data['artwork_price'] = result.ARTWORK_PRICE.price
                dict_data['is_customed'] = result.is_customed
                dict_data['custom_info'] = result.custom_info

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
    def get(self, request):
        user = User.objects
        order = Order.objects.select_related(
            'user',
            'artwork',
            'artwork_color',
            'artwork_price',
            'order_status'
        ).filter(user=request.user.id, order_status=3).order_by('id')

        try:
            orders = list()
            user_data = dict()

            user_data['email'] = user.email
            user_data['mobile_number'] = user.mobile_number
            user_data['first_name'] = user.first_name
            user_data['last_name'] = user.last_name
            user_data['address'] = user.address
            user_data['zipcode'] = user.zipcode

            for result in order:
                dict_data = dict()
                dict_data['id'] = result.id
                dict_data['user'] = result.user.name
                dict_data['artwork'] = result.artwork.name
                dict_data['artwork_color'] = result.artwork_color.name
                dict_data['artwork_price'] = result.artwork_price.price
                dict_data['is_customed'] = result.is_customed
                dict_data['custom_info'] = result.custom_info
                dict_data['order_status'] = result.order_status.name

                orders.append(dict_data)

            return JsonResponse({
                "user_data": user_data,
                "orders": orders,
            }, status=200)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)

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

            for id in data['id']:
                Order.objects.filter(id=id).update(order_status_id=data['order_status_id'])

            email(data, user)
            # self.sms_service(data, user)
            return HttpResponse(status=200)

        except Order.DoesNotExist:
            return JsonResponse({"message": "INVALID_VALUE"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)
