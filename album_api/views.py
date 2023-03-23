from django.shortcuts import render
from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.exceptions import ValidationError


class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post = AlbumReview.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, content=post)


class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima trinti svetimų pranešimų!')

    def put(self, request, *args, **kwargs):
        post = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima koreguoti svetimų pranešimų!')


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewCommentList(generics.ListCreateAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        albumreview = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewComment.objects.filter(album_review=albumreview)


class AlbumReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        comment = AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if comment.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima trinti svetimų komentarų!')

    def put(self, request, *args, **kwargs):
        comment = AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if comment.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima koreguoti svetimų komentarų!')


class AlbumReviewLikeList(generics.ListCreateAPIView):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
