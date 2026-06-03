
from django.shortcuts import get_object_or_404 # type:ignore[import]
from django.core.files.storage import FileSystemStorage # type:ignore[import]
from django.shortcuts import render # type:ignore[import]
from .serializers import StudentSerializer # type:ignore[import]
from .serializers import FrameSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView # type:ignore[import]
# from django.views import View
import datetime
import json
from django.views.decorators.csrf import csrf_exempt # type:ignore[import]
from django.views.decorators.http import require_http_methods # type:ignore[import]
from django.http import JsonResponse # type:ignore[import]
from django.http import JsonResponse # type:ignore[import]
from django.shortcuts import get_object_or_404 # type:ignore[import]

from django.http import JsonResponse # type:ignore[import]
from .models import Students
from .models import Frame
import base64
from io import BytesIO
from PIL import Image
# Create your views here.


class FrameList(ListCreateAPIView):
    queryset = Frame.objects.all()
    serializer_class = FrameSerializer

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("yes post is working ")
            frameName = request.POST.get('frameName')
            frameType = request.POST.get('frameType')
            frameComment = request.POST.get('frameComment')
            frameImage = request.POST.get('frameImage')
            print("name", frameName)
            print("type", frameType)
            print("comment", frameComment)
            # print("image", frameImage)
            if frameName:
                # decode the base64 image data into bytes
                # remove the "data:image/jpeg;base64," prefix
                data = frameImage.split(',')[1]
                image_bytes = base64.b64decode(data)
                image = Image.open(BytesIO(image_bytes))
                # generate a new filename based on the current timestamp
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f'captured_frame_{timestamp}.jpg'

                # save the image to a file with the new filename
                image.save(filename)

                # create a new Frame object and save it to the database
                frame_data = Frame(frame_name=frameName, frame_type=frameType,
                                   frame_comment=frameComment, frame_image=filename)
                frame_data.save()

            return JsonResponse({'message': 'frame data created successfully'})
        return JsonResponse({'error': 'Invalid request method'})


class StudentList(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
