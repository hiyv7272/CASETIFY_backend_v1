import jwt
import requests

from django.http import JsonResponse
from django.core import validators
from django.core.mail.message import EmailMessage
from casetify_backend.settings import SECRET_KEY
from my_settings import SMS_AUTH_ID, SMS_SERVICE_SECRET, SMS_FROM_NUMBER, SMS_URL

from .models import User
from order.models import Order


def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload = jwt.decode(access_token, SECRET_KEY, algorithm='HS256')
            user = User.objects.get(id=payload["id"])
            request.user = user
        except jwt.DecodeError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=400)
        except TypeError:
            return JsonResponse({'message': 'INVALID_VALUE'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID'}, status=400)
        return func(self, request, *args, **kwargs)

    return wrapper


class ValidateData(object):
    def __init__(self, data):
        self.data = data

    def password(self):
        print(self.data['password'])
        if len(self.data['password']) < 8:
            return JsonResponse({'message': 'INVALID_PASSWORD'}, status=400)

        return None

    def email(self):
        print(self.data['email'])

        if validators.validate_email(self.data['email']):
            return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)

        if User.objects.filter(email=self.data['email']).exists():
            return JsonResponse({'message': 'DUPLICATE_EMAIL'}, status=401)

        return None


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