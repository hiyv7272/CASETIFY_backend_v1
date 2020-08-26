import json

from datetime import datetime
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from user.utils import login_decorator

from .models import Order, Orderer, CheckoutStatus, CheckOut, Cart
from user.models import User
from artwork.models import Phonecase, PhonecasePrice


class CartView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            phonecase_price = PhonecasePrice.objects.all()

            Cart.objects.create(
                USER=User.objects.get(id=request.user.id),
                PHONECASE=Phonecase.objects.get(id=data['phonecase_id']),
                PHONECASE_PRICE=phonecase_price.get(PHONECASE=data['phonecase_id']),
                is_custom=data['is_custom'],
                custom_info=data['custom_info'],
                quantity=data['quantity'],
                is_use=True
            )

            return HttpResponse(status=200)

        except Cart.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except KeyError:
            return JsonResponse({'message': "INVALID_KEYS"}, status=400)

    @login_decorator
    def get(self, request):
        try:
            custom_cart = Cart.objects.select_related(
                'USER',
                'PHONECASE',
                'PHONECASE_PRICE'
            ).select_related(
                'PHONECASE__FEATURED',
                'PHONECASE__DEVICE_MODEL',
                'PHONECASE__PHONECASE_COLOR',
                'PHONECASE__PHONECASE_TYPE',
                'PHONECASE__ARTWORK'
            ).filter(USER=request.user.id, is_custom=True, is_use=True).order_by('id')

            regular_cart = Cart.objects.select_related(
                'USER',
                'PHONECASE',
                'PHONECASE_PRICE'
            ).select_related(
                'PHONECASE__FEATURED',
                'PHONECASE__DEVICE_MODEL',
                'PHONECASE__PHONECASE_COLOR',
                'PHONECASE__PHONECASE_TYPE',
                'PHONECASE__ARTWORK'
            ).filter(USER=request.user.id, is_custom=False, is_use=True).order_by('id')

            custom_cart_list = list()
            for row in custom_cart:
                dict_data = dict()
                dict_data['cart_id'] = row.id
                dict_data['phonecase_id'] = row.PHONECASE.id
                dict_data['phonecase_name'] = row.PHONECASE.name
                dict_data['phonecase_device_name'] = row.PHONECASE.DEVICE_MODEL.name
                dict_data['phonecase_color_name'] = row.PHONECASE.PHONECASE_COLOR.name
                dict_data['phonecase_type'] = row.PHONECASE.PHONECASE_TYPE.name
                dict_data['phonecase_price'] = row.PHONECASE_PRICE.price
                dict_data['phonecase_artwork_name'] = row.PHONECASE.ARTWORK.name
                dict_data['is_custom'] = row.is_custom
                dict_data['custom_info'] = row.custom_info
                dict_data['quantity'] = row.quantity

                custom_cart_list.append(dict_data)

            regular_cart_list = list()
            for row in regular_cart:
                dict_data = dict()
                dict_data['cart_id'] = row.id
                dict_data['phonecase_id'] = row.PHONECASE.id
                dict_data['phonecase_name'] = row.PHONECASE.name
                dict_data['phonecase_device_name'] = row.PHONECASE.DEVICE_MODEL.name
                dict_data['phonecase_color_name'] = row.PHONECASE.PHONECASE_COLOR.name
                dict_data['phonecase_type'] = row.PHONECASE.PHONECASE_TYPE.name
                dict_data['phonecase_price'] = row.PHONECASE_PRICE.price
                dict_data['phonecase_artwork_name'] = row.PHONECASE.ARTWORK.name
                dict_data['is_custom'] = row.is_custom
                dict_data['custom_info'] = row.custom_info
                dict_data['quantity'] = row.quantity

                regular_cart_list.append(dict_data)

            return_data = dict()
            return_data['custom_order'] = custom_cart_list
            return_data['regular_order'] = regular_cart_list

            return JsonResponse({'data': return_data}, status=200)

        except Cart.DoesNotExist:
            return JsonResponse({"message": "INVALID_VALUE"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)


class CheckoutView(View):
    @login_decorator
    def post(self, request):
        with transaction.atomic():
            try:
                delivery_price = float("5.99")
                sub_total_price = float("00.00")
                order_number = datetime.now().strftime('%Y%m%d%H%m%s')
                user_id = request.user.id

                orderer = Orderer.objects.get(USER=user_id)
                orderer.USER = User.objects.get(id=user_id)
                orderer.first_name = request.GET.get('first_name')
                orderer.last_name = request.GET.get('last_name')
                orderer.address = request.GET.get('address')
                orderer.zipcode = request.GET.get('zipcode')
                orderer.mobile_number = request.GET.get('mobile_number')
                orderer.save()

                for cart_id in request.GET.get('cart_id').split(','):
                    cart = Cart.objects.get(id=cart_id)
                    if cart:
                        cart.is_use = False
                        cart.save()
                        sub_total_price += float(Cart.objects.select_related('PHONECASE_PRICE').get(id=cart_id).PHONECASE_PRICE.price)

                if sub_total_price > 49.00:
                    delivery_price = float("00.00")

                total_price = sub_total_price + delivery_price

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
                        sell_price=Cart.objects.select_related('PHONECASE_PRICE').get(id=cart_id).PHONECASE_PRICE.price,
                        is_use=True
                    ).save()

                return HttpResponse(status=200)

            except Orderer.DoesNotExist:
                return JsonResponse({'message': "INVALID_VALUE"}, status=400)
            except User.DoesNotExist:
                return JsonResponse({'message': "INVALID_VALUE"}, status=400)
            except Cart.DoesNotExist:
                return JsonResponse({'message': "INVALID_VALUE"}, status=400)
            except KeyError:
                return JsonResponse({'message': "INVALID_KEYS"}, status=400)

    @login_decorator
    def get(self, request):
        try:
            order = Order.objects.select_related(
                'USER',
                'ORDERER'
            ).all().filter(USER=request.user.id)

            order_list = list()
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

            return JsonResponse({'data': order_list}, status=200)

        except Order.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)


class CheckoutDetailView(View):
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

            return JsonResponse({'data': checkout_list}, status=200)

        except CheckOut.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)
