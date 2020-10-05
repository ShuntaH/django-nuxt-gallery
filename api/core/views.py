from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import PhotosSerializer
from .models import Photos


# Create your views here.
class PhotosViewSet(viewsets.ModelViewSet):
    serializer_class = PhotosSerializer
    queryset = Photos.objects.all()
