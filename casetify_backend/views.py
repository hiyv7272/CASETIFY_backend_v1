import boto3
from django.views import View
from django.http import JsonResponse
from my_settings import S3_CONFIG


class FileToUrl(View):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=S3_CONFIG['S3_ACCESS_KEY'],
        aws_secret_access_key=S3_CONFIG['S3_SECRET_KEY'],
    )

    def post(self, request):
        for file in request.FILES.getlist('files'):
            self.s3_client.upload_fileobj(
                file,
                S3_CONFIG['S3_BUCKET'],
                file.name,
                ExtraArgs={
                    "ContentType": file.content_type
                }
            )
        file_urls = [f"https://s3.ap-northeast-2.amazonaws.com/{S3_CONFIG['S3_BUCKET']}/{file.name}" for file in request.FILES.getlist('files')]

        return JsonResponse({"file_urls": file_urls}, status=200)