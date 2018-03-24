from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JujinSerializer
from .models import Juejin
# Create your views here.

class JuejinViewSet(viewsets.ModelViewSet):
    queryset = Juejin.objects.all()
    serializer_class = JujinSerializer
    pagination_class = None

