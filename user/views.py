import jwt
import json
import bcrypt
import requests

from django.views import View
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from casetify_backend.settings import SECRET_KEY

from .models import User
from order.models import Orderer
from .utils import login_decorator, validate_password, validate_email


class SignUpView(View):
    def post(self, request):
        with transaction.atomic():

            try:
                data = json.loads(request.body)

                validated_password = validate_password(data)
                if validated_password:
                    return validated_password

                validated_email = validate_email(data)
                if validated_email:
                    return validated_email

                hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode()
                User(
                    email=data['email'],
                    password=hashed_password,
                    mobile_number=data['mobile_number'],
                    is_use=True
                ).save()

                Orderer(
                    USER=User.objects.get(email=data['email'])
                ).save()

                return HttpResponse(status=200)

            except TypeError:
                return JsonResponse({'message': 'INVALID_TYPE'}, status=400)
            except KeyError:
                return JsonResponse({'message': 'INVALID_KEYS'}, status=400)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            user = User.objects.get(email=data['email'])

            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                access_token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm='HS256')
                return JsonResponse({'access_token': access_token.decode('utf-8')}, status=200)

            return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)


class MyProfileView(View):
    @login_decorator
    def get(self, request):
        user = User.objects.get(id=request.user.id)

        try:
            result = dict()
            result['name'] = user.name
            result['email'] = user.email
            result['mobile_number'] = user.mobile_number
            result['first_name'] = user.first_name
            result['last_name'] = user.last_name
            result['introduction'] = user.introduction
            result['website'] = user.website_url
            result['location'] = user.location
            result['twitter'] = user.twitter
            result['image'] = user.profile_image_url

            return JsonResponse(result, status=200)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)

    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(id=request.user.id)

        try:
            user.name = data['name']
            user.bio = data['introduction']
            user.website_url = data.get('website')
            user.location = data.get('location')
            user.twitter = data.get('twitter')
            user.profile_image_url = data.get('images')
            user.save()

            return HttpResponse(status=200)

        except user.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)


class MyShippingInfoView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(id=request.user.id)

        try:
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.address = data['address']
            user.zipcode = data['zipcode']
            user.mobile_number = data['mobile_number']
            user.save()

            return HttpResponse(status=200)

        except user.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)


class KakaologinView(View):
    def post(self, request):

        try:
            kakao_token = request.headers["Authorization"]
            print('kt', kakao_token)
            headers = ({"Authorization": f"Bearer {kakao_token}"})
            url = "https://kapi.kakao.com/v1/user/me"
            response = requests.get(url, headers=headers)
            print('kakao re', response.json)
            kakao_user = response.json()
            print(kakao_user)

            if User.objects.filter(kakao_id=kakao_user["id"]).exists():
                user_id = User.objects.get(kakao_id=kakao_user["id"]).id
                print('user_id', user_id)
                access_token = jwt.encode({'id': user_id}, SECRET_KEY, algorithm="HS256")
                print('access_token', access_token)
                return JsonResponse({"access_token": access_token.decode('utf-8')}, status=200)

            else:
                newUser = User.objects.create(
                    kakao_id=kakao_user["id"],
                    email=kakao_user["kaccount_email"],
                    name=kakao_user["properties"]["nickname"]
                )
                access_token = jwt.encode({'id': newUser.id}, SECRET_KEY, algorithm="HS256")
                return JsonResponse({"access_token": access_token.decode('utf-8')}, status=200)

        except KeyError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=400)
        except kakao_token.DoesNotExist:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=400)

