from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

api_v1 = DefaultRouter()

api_v1.register('posts', PostViewSet, basename='posts')
api_v1.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments'
)
api_v1.register('groups', GroupViewSet, basename='groups')
api_v1.register('follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(api_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
