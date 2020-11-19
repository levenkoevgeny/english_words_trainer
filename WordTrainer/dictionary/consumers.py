import json

from channels.generic.websocket import WebsocketConsumer
from dictionary.models import Word

import random


class TrainingConsumer(WebsocketConsumer):
    def connect(self):
        dictionary_id = self.scope['url_route']['kwargs']['dictionary_id']
        words = Word.objects.filter(dictionary_id=dictionary_id)
        id_list = []
        for word in words:
            id_list.append(word.id)

        random_id = random.randint(0, len(id_list)-1)
        random_word = Word.objects.get(pk=id_list[random_id])

        self.accept()

        self.send(text_data=json.dumps({
            'foreign': random_word.foreign_meaning,
            'native': random_word.native_meaning
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass
