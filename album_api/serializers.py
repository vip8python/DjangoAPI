from rest_framework import serializers
from .models import *


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_review = serializers.ReadOnlyField(source='albumreview.id')

    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'user', 'user_id', 'content', 'album_review']


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_review_count = serializers.SerializerMethodField()
    album_review = serializers.StringRelatedField(many=True)

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'album_review_count', 'album_review', 'user_id', 'album', 'content', 'score']

    def get_album_review_count(self, obj):
        return AlbumReviewComment.objects.filter(album_review=obj).count()


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


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReviewLike
        fields = ['id', 'user', 'user_id', 'album_review']
