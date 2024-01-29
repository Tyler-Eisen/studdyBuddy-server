from studybuddyapi.views import TopicView,OpenAIView, UserView, ConversationContextView
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'topics', TopicView, 'topic')
router.register(r'ai', OpenAIView, 'ai')
router.register(r'users', UserView, 'user')
router.register(r'conversation_context', ConversationContextView, 'conversation_context')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
