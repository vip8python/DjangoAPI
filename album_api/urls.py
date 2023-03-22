from django.urls import path, include
from .views import *

urlpatterns = [
    path('review/', AlbumReviewList.as_view()),
    path('song/', SongList.as_view()),
    path('band/', BandList.as_view()),
    path('album/', AlbumList.as_view()),
    path('comment/', AlbumReviewCommentList.as_view()),
    path('like/', AlbumReviewLikeList.as_view()),
]