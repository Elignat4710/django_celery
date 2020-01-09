from django.urls import re_path
from django.urls import path
from .consumers import CompanyListConsumer


websocket_urlpatterns = [
    re_path(r'ws/$', CompanyListConsumer),
]
