from django.urls import path
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from .views import PostList

app_name='blog_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls


