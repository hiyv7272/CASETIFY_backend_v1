import json

from datetime import datetime
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from user.utils import login_decorator

from .models import Order, Orderer, CheckoutStatus, CheckOut, Cart
from user.models import User
from artwork.models import Artwork, ArtworkPrice


class CartView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)

        try:
            print(data)
            artwork_price = ArtworkPrice.objects.all()
            Cart.objects.create(
                USER=User.objects.get(id=request.user.id),
                ARTWORK=Artwork.objects.get(id=data['artwork_id']),
                ARTWORK_PRICE=artwork_price.get(ARTWORK=data['artwork_id']),
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

                for cart_id in request.GET.get('cart_id').split(','):
                    cart = Cart.objects.get(id=cart_id)
                    cart.is_use = False
                    cart.save()
                    sub_total_price += float(Cart.objects.select_related('ARTWORK_PRICE').get(id=cart_id).ARTWORK_PRICE.price)

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

            return JsonResponse({"data": checkout_list}, status=200)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)
