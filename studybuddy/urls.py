from studybuddyapi.views import TopicView,OpenAIView
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'topics', TopicView, 'topic')
router.register(r'ai', OpenAIView, 'ai')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
