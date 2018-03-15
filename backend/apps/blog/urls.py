# bulid by Bean_Wei/ 2018/3/13 11:00
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'tags',TagViewSet,'tags')
router.register(r'category', CategoryViewSet, 'category')
router.register(r'articles', PostViewSet, 'post')

app_name = 'blog'
urlpatterns = router.urls