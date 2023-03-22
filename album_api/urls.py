from django.urls import path, include
from .views import *

urlpatterns = [
    path('posts/', AlbumReviewList.as_view()),
    path('song/', SongList.as_view()),
]