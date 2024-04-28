from django.urls import path
from app1.views import language, months


urlpatterns = [
    path('language', language),
    path('months', months)
]