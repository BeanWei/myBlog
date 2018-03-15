# bulid by Bean_Wei/ 2018/3/13 11:04
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source='get_post_count', read_only=True)

    class Meta:
        model = Tag
        fields = ('name','slug','count')

class CategorySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source='get_post_count', read_only=True)

    class Meta:
        model = Category
        fields = ('name','slug','count')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.CharField(source='get_tags')
    tagsSlug = serializers.CharField(source='get_tags_slug', read_only=True)
    category = serializers.CharField(source='category.name')
    categorySlug = serializers.CharField(source='category.slug', read_only=True)
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    html = serializers.CharField(source='get_html_content', read_only=True)
    synopsis = serializers.CharField(source='get_synopsis', read_only=True)
    readNum = serializers.IntegerField(source='read_num')

    class Meta:
        model = Post
        fields = ('url', 'own', 'title', 'category','categorySlug','tags','tagsSlug','slug','timestamp', 'html', 'synopsis', 'readNum')
        extra_kwargs = {
            'url': {'view_name': 'blog:post-detail','lookup_field': 'slug'}
        }

    def __init__(self, *args, **kwargs):
        # Don't pass the 'detail' arg up to the superclass
        detail = kwargs.pop('detail', False)
        super(PostSerializer, self).__init__(*args, **kwargs)

        if not detail:
            self.fields.pop('html')
        else:
            self.fields.pop('url')