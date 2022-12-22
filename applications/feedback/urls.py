from rest_framework.routers import DefaultRouter
from django.urls import path, include

from applications.feedback.views import CommentApiView, FavoriteApiView

router = DefaultRouter()
router.register('comment', CommentApiView)
router.register('comment', FavoriteApiView)

urlpatterns = [
    path('', include(router.urls))

]
