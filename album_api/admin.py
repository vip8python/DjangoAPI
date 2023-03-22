from django.contrib import admin
from.models import *

admin.site.register(Band)
admin.site.register(Album)
admin.site.register(AlbumReview)
admin.site.register(Song)
admin.site.register(AlbumReviewComment)
admin.site.register(AlbumReviewLike)

