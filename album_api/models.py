from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Album(models.Model):
    name = models.CharField(max_length=200)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Song(models.Model):
    name = models.CharField(max_length=150)
    duration = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
    ])
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.duration}'


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=1000)
    score = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
    ])

    def __str__(self):
        return f'{self.content} {self.score}'


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='album_review')
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.content}'


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, null=True, blank=True)
