from studybuddyapi.views import TopicView
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'topics', TopicView, 'topic')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
