from django.contrib import admin

from applications.feedback.models import Rating, Comment, Like, Favorite

# Register your models here.
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Like)
admin.site.register(Favorite)