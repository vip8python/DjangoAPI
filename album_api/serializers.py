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
    likes = serializers.SerializerMethodField()

    class Meta:
        model = AlbumReview
        # fields = ['id', 'user', 'image', 'likes', 'album_review_count', 'album_review', 'user_id', 'album', 'content', 'score']
        fields = '__all__'

    def get_album_review_count(self, obj):
        return AlbumReviewComment.objects.filter(album_review=obj).count()

    def get_likes(self, post):
        return AlbumReviewLike.objects.filter(album_review=post).count()


class SongSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Song
        # fields = ['id', 'name', 'user', 'user_id', 'duration', 'album']
        fields = "__all__"


class BandSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Band
        # fields = ['id', 'user', 'user_id', 'name']
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Album
        # fields = ['id', 'user', 'user_id', 'name', 'band']
        fields = "__all__"


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReviewLike
        # fields = ['id', 'user', 'user_id', 'album_review']
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
