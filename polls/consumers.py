from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class CompanyListConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'companies_list',
            self.channel_name
        )
        self.accept()

    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            'companies_list',
            self.channel_name
        )

    def reload_page(self, event):
        reload_page = event['reload_page']
        self.send(text_data=json.dumps({
            'reload_page': reload_page
        }))
