from rest_framework import serializers
from .models import *

class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_id', 'album', 'content', 'score']

class SongSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Song
        fields = ['id', 'name', 'user', 'user_id', 'duration', 'album']

class BandSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Band
        fields = ['id', 'user', 'user_id', 'name']

class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Album
        fields = ['id', 'user', 'user_id', 'name', 'band']


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'user', 'user_id', 'user', 'content', 'album_review']


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')


    class Meta:
        model = AlbumReviewLike
        fields = ['id', 'user', 'user_id', 'album_review']



