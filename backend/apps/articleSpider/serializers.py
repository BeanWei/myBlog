from rest_framework import serializers
from apps.articleSpider.models import Juejin

class JujinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juejin
        fields = '__all__'