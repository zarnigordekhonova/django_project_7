from django.urls import path
from app2.views import price, your_level


urlpatterns = [
    path('price', price),
    path('level', your_level)
]