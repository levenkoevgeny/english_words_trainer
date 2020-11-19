from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/training/(?P<dictionary_id>\w+)/$', consumers.TrainingConsumer.as_asgi()),
]