from django.views import View
from django.http import JsonResponse
from django.db.models import Count

from .models import (
    Artist,
    Artwork,
    ArtworkImage,
    ArtworkPrice,
    ArtworkReview,
    ArtworkType
)


class ArtworkListView(View):
    def get(self, request):
        artwork = Artwork.objects.select_related(
            'FEATURED',
            'DEVICE',
            'ARTWORK_COLOR',
            'ARTWORK_TYPE',
            'ARTIST'
        ).all().filter(ARTWORK_TYPE=ArtworkType.objects.get(name='Impact'))
        artwork_image = ArtworkImage.objects.all()
        artwork_price = ArtworkPrice.objects.all()
        artist = Artist.objects.all()

        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 8)) + offset

        artwork_list = list()
        for row in artist:
            dict_data = dict()
            dict_data['artist_id'] = row.id
            dict_data['artist_name'] = row.name
            dict_data['artist_description'] = row.description
            dict_data['artwork_color'] = list()

            artwork_list.append(dict_data)

        for el in artwork_list:
            for row in artwork[offset:limit]:
                if el['artist_id'] == row.ARTIST.id:
                    el['artwork_type'] = row.ARTWORK_TYPE.name
                    el['artwork_price'] = artwork_price.get(ARTWORK=row.id).price
                    el['artwork_image_url'] = artwork_image.get(ARTWORK=row.id).image_url_1
                    dict_data = dict()
                    dict_data['artwork_id'] = row.id
                    dict_data['artwork_color_id'] = row.ARTWORK_COLOR.id
                    dict_data['artwork_color_name'] = row.ARTWORK_COLOR.name
                    dict_data['artowkr_color_info'] = row.ARTWORK_COLOR.info
                    el['artwork_color'].append(dict_data)

        return JsonResponse({"data": artwork_list}, status=200)


class ArtworkDetailView(View):
    def get(self, request):
        artist_id = request.GET.get('artist_id')
        artwork_id = request.GET.get('artwork_id')

        artwork = Artwork.objects.select_related(
            'FEATURED',
            'DEVICE',
            'ARTWORK_COLOR',
            'ARTWORK_TYPE',
            'ARTIST'
        ).all()

        artwork_review = ArtworkReview.objects.select_related('USER').filter(ARTWORK=artwork_id)

        artwork_image = ArtworkImage.objects.all()

        artwork_price = ArtworkPrice.objects.all()

        # device_list
        device_list = list()

        for row in artwork.values('FEATURED__id', 'DEVICE__id', 'DEVICE__name').annotate(Count('DEVICE')):
            dict_data = dict()
            dict_data['featured_id'] = row['FEATURED__id']
            dict_data['device_id'] = row['DEVICE__id']
            dict_data['device_name'] = row['DEVICE__name']
            device_list.append(dict_data)

        # artwork_list
        artwork_list = list()

        for artwork_row in artwork.filter(ARTIST=artist_id):
            dict_data = dict()
            dict_data['artwork_id'] = artwork_row.id
            dict_data['artwork_type_id'] = artwork_row.ARTWORK_TYPE.id
            dict_data['artwork_type_name'] = artwork_row.ARTWORK_TYPE.name
            dict_data['artwork_color_id'] = artwork_row.ARTWORK_COLOR.id
            dict_data['artwork_color_name'] = artwork_row.ARTWORK_COLOR.name
            dict_data['artwork_color_info'] = artwork_row.ARTWORK_COLOR.info
            dict_data['artwork_price'] = artwork_price.get(ARTWORK=artwork_row.id).price

            dict_data['artwork_images'] = list()
            for images_row in artwork_image.filter(ARTWORK=artwork_row.id):
                images_dict_data = dict()
                images_dict_data['image_url_1'] = images_row.image_url_1
                images_dict_data['image_url_2'] = images_row.image_url_2
                images_dict_data['iamge_url_3'] = images_row.image_url_3
                images_dict_data['iamge_url_4'] = images_row.image_url_4
                images_dict_data['iamge_url_5'] = images_row.image_url_5
                images_dict_data['iamge_url_6'] = images_row.image_url_6

                dict_data['artwork_images'].append(images_dict_data)

            artwork_list.append(dict_data)

        # select_artwork_info
        select_artwork_info = dict()

        for artwork_info_row in artwork.filter(id=artwork_id):
            select_artwork_info['artwork_id'] = artwork_info_row.id
            select_artwork_info['artwork_name'] = artwork_info_row.id
            select_artwork_info['artwork_description'] = artwork_info_row.description
            select_artwork_info['artwork_is_custom'] = artwork_info_row.is_custom
            select_artwork_info['artwork_is_use'] = artwork_info_row.is_use

        # artwork_review_list
        artwork_review_list = list()

        for artwork_review_row in artwork_review:
            dict_data = dict()
            dict_data['user_id'] = artwork_review_row.USER.id
            dict_data['uesr_name'] = artwork_review_row.USER.name
            dict_data['title'] = artwork_review_row.title
            dict_data['comment'] = artwork_review_row.comment
            dict_data['rate'] = artwork_review_row.rate
            dict_data['update_datetime'] = artwork_review_row.update_datetime

            artwork_review_list.append(dict_data)

        return JsonResponse({
            "device_list": device_list,
            "artwork_list": artwork_list,
            "select_artwork_info": select_artwork_info,
            "artwork_review_list": artwork_review_list
        }, status=200)

