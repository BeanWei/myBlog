from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.decorators import list_route
from .models import *
from .serializers import *
# Create your views here.

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().filter(published=True)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    lookup_value_regex = r'\w+'

    def get_queryset(self):
        query_set = super().get_queryset()
        #获取请求参数---》slug后缀
        category = self.request.query_params.get('category',None)
        tags = self.request.query_params.get('tag',None)
        archive = self.request.query_params.get('archive', None)
        if category is not None:
            query_set = query_set.filter(category__slug=category)
        if tags is not None:
            query_set = query_set.filter(tags__slug=tags)
            #query_set = Tag.objects.get(slug=tags).post_set.all()
        if archive is not None:
            if len(archive) != 6:
                raise ParseError
            query_set = query_set.filter(timestamp__year=archive[:4], timestamp__month=archive[4:6])
        return query_set

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        instance.read_num += 1
        instance.save()
        serializer = self.get_serializer(instance,detail=True)

        return Response(serializer.data)

    @list_route(url_path='archive')
    def date_archive(self,request):
        archives = []
        timestamp_month = self.queryset.dates('timestamp', 'month', order='DESC')
        for pub in timestamp_month:
            #num = self.queryset.filter(timestamp__year=pub.year, timestamp__month=int(pub.month)).count()
            '''%02d 0为占位符 占2位 月份为2位，不然无法查询，哲理需要转化一下格式，1-9月前面补零'''
            num = self.queryset.filter(timestamp__startswith="%d-%02d" % (pub.year, pub.month)).count()
            archives.append({'record': '{:d}年{:d}月'.format(pub.year, pub.month),  'num': num})

        return Response(archives)