from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, ListAPIView, DestroyAPIView

from .models import Covid19C
from .serializers import covid19Serializer

# Create your views here.


class CreateRecords(ListCreateAPIView):
    queryset  = Covid19C.objects.all()
    serializer_class = covid19Serializer

class ViewRecords(ListAPIView):
    queryset = Covid19C.objects.all()
    serializer_class = covid19Serializer

class DeleteRecords(DestroyAPIView):
    queryset = Covid19C.objects.all()
    serializer_class = covid19Serializer