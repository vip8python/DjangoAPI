from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    name = models.CharField(max_length=200)


class Album(models.Model):
    name = models.CharField(max_length=200)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True, blank=True)


class Song(models.Model):
    name = models.CharField(max_length=150)
    duration = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
    ])
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=1000)
    score = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
    ])


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=1000)


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, null=True, blank=True)
