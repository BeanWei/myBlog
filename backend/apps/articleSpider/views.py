from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JujinSerializer
from apps.articleSpider.models import Juejin
# Create your views here.

class JuejinViewSet(viewsets.ModelViewSet):
    queryset = Juejin.objects.all()
    serializer_class = JujinSerializer
    pagination_class = None

