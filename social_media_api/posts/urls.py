from django.urls import path, include
from .views import FeedView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'feed', FeedView, basename='feed')

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),

    path('"feed/"', include(feeds.urls))
    path('', include(router.urls)),
]
