from django.urls import path, include
from .views import *

urlpatterns = [
    path('reviews/', AlbumReviewList.as_view()),
    path('reviews/<int:pk>/', AlbumReviewDetail.as_view()),
    path('reviews/<int:pk>/comments/', AlbumReviewCommentList.as_view()),

    path('songs/', SongList.as_view()),
    path('bands/', BandList.as_view()),
    path('albums/', AlbumList.as_view()),
    # path('comments/', AlbumReviewCommentList.as_view()),
    path('comments/<int:pk>/', AlbumReviewCommentDetail.as_view()),

    path('likes/', AlbumReviewLikeList.as_view()),
    path('reviews/<int:pk>/like/', AlbumReviewLikeCreate.as_view()),

    path('signup', UserCreate.as_view()),
]