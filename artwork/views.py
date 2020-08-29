from django.views import View
from django.http import JsonResponse
from django.db.models import Count

from .models import (
    Artwork,
    Phonecase,
    PhonecaseImage,
    PhonecasePrice,
    PhonecaseReview,
    PhonecaseType
)


class ArtworkListView(View):
    def get(self, request):
        try:
            phonecase = Phonecase.objects.select_related(
                'FEATURED',
                'DEVICE_MODEL',
                'PHONECASE_COLOR',
                'PHONECASE_TYPE',
                'ARTWORK'
            ).all().filter(PHONECASE_TYPE=PhonecaseType.objects.get(name='Impact'))
            phonecase_image = PhonecaseImage.objects.all()
            phonecase_price = PhonecasePrice.objects.all()
            artwork = Artwork.objects.all()

            offset = int(request.GET.get('offset', 0))
            limit = int(request.GET.get('limit', 8)) + offset

            artwork_list = list()
            for row in artwork[offset:limit]:
                dict_data = dict()
                dict_data['artwork_id'] = row.id
                dict_data['artwork_name'] = row.name
                dict_data['artwork_description'] = row.description
                dict_data['phonecase_color'] = list()

                artwork_list.append(dict_data)

            for el in artwork_list:
                for row in phonecase:
                    if el['artwork_id'] == row.ARTWORK.id:
                        el['phonecase_type'] = row.PHONECASE_TYPE.name
                        el['phonecase_price'] = phonecase_price.get(PHONECASE=row.id).price
                        el['phonecase_image_url'] = phonecase_image.get(PHONECASE=row.id).image_url_1
                        dict_data = dict()
                        dict_data['phonecase_id'] = row.id
                        dict_data['phonecase_color_id'] = row.PHONECASE_COLOR.id
                        dict_data['phonecase_color_name'] = row.PHONECASE_COLOR.name
                        dict_data['phonecase_color_info'] = row.PHONECASE_COLOR.info
                        el['phonecase_color'].append(dict_data)

            return JsonResponse({'data': artwork_list}, status=200)

        except Phonecase.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except PhonecaseType.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except PhonecaseImage.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except PhonecasePrice.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except KeyError:
            return JsonResponse({'message': "INVALID_KEYS"}, status=400)


class ArtworkDetailView(View):
    def get(self, request):
        try:
            artwork_id = request.GET.get('artwork_id')
            phonecase_id = request.GET.get('phonecase_id')

            phonecase = Phonecase.objects.select_related(
                'FEATURED',
                'DEVICE_MODEL',
                'PHONECASE_COLOR',
                'PHONECASE_TYPE',
                'ARTWORK'
            ).all()

            phonecase_review = PhonecaseReview.objects.select_related('USER').filter(PHONECASE=phonecase_id)

            phonecase_image = PhonecaseImage.objects.all()

            phonecase_price = PhonecasePrice.objects.all()

            # device_list
            device_list = list()
            for row in phonecase.filter(ARTWORK=artwork_id).values('FEATURED__id', 'DEVICE_MODEL__id', 'DEVICE_MODEL__name').distinct():
                dict_data = dict()
                dict_data['featured_id'] = row['FEATURED__id']
                dict_data['device_model_id'] = row['DEVICE_MODEL__id']
                dict_data['device_model_name'] = row['DEVICE_MODEL__name']

                device_list.append(dict_data)

            # PHONECASE_list
            phonecase_list = list()
            for row in phonecase.filter(ARTWORK=artwork_id):
                dict_data = dict()
                dict_data['phonecase_id'] = row.id
                dict_data['phoecase_model_name'] = row.name
                dict_data['phonecase_type_id'] = row.PHONECASE_TYPE.id
                dict_data['phonecase_type_name'] = row.PHONECASE_TYPE.name
                dict_data['phonecase_color_id'] = row.PHONECASE_COLOR.id
                dict_data['phonecase_color_name'] = row.PHONECASE_COLOR.name
                dict_data['phonecase_color_info'] = row.PHONECASE_COLOR.info
                dict_data['phonecase_price'] = phonecase_price.get(PHONECASE=row.id).price

                dict_data['phonecase_images'] = list()
                for images_row in phonecase_image.filter(PHONECASE=row.id):
                    images_dict_data = dict()
                    images_dict_data['image_url_1'] = images_row.image_url_1
                    images_dict_data['image_url_2'] = images_row.image_url_2
                    images_dict_data['iamge_url_3'] = images_row.image_url_3
                    images_dict_data['iamge_url_4'] = images_row.image_url_4
                    images_dict_data['iamge_url_5'] = images_row.image_url_5
                    images_dict_data['iamge_url_6'] = images_row.image_url_6

                    dict_data['phonecase_images'] = images_dict_data

                phonecase_list.append(dict_data)

            # select_phonecase_info
            select_phonecase_info = dict()
            for row in phonecase.filter(id=phonecase_id):
                select_phonecase_info['phonecase_id'] = row.id
                select_phonecase_info['phonecase_model_name'] = row.name
                select_phonecase_info['phonecase_name'] = row.id
                select_phonecase_info['phonecase_description'] = row.description
                select_phonecase_info['phonecase_is_custom'] = row.is_custom
                select_phonecase_info['phonecase_is_use'] = row.is_use

            # phonecase_review_list
            phonecase_review_list = list()

            for row in phonecase_review:
                dict_data = dict()
                dict_data['user_id'] = row.USER.id
                dict_data['uesr_name'] = row.USER.name
                dict_data['title'] = row.title
                dict_data['comment'] = row.comment
                dict_data['rate'] = row.rate
                dict_data['update_datetime'] = row.update_datetime

                phonecase_review_list.append(dict_data)

            return_data = dict()
            return_data['device_list'] = device_list
            return_data['phonecase_list'] = phonecase_list
            return_data['select_phonecase_info'] = select_phonecase_info
            return_data['phonecase_review_list'] = phonecase_review_list

            return JsonResponse({'data': return_data}, status=200)

        except Phonecase.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except PhonecaseType.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except PhonecaseImage.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except PhonecasePrice.DoesNotExist:
            return JsonResponse({'message': "INVALID_VALUE"}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)