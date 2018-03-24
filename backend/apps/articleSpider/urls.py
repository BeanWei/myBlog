from rest_framework.routers import DefaultRouter
from .views import JuejinViewSet

router = DefaultRouter()
router.register(r'articlespider',JuejinViewSet,'articlespider')

app_name = 'articleSpider'
urlpatterns = router.urls