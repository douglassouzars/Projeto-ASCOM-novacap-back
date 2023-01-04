from django.urls import path
from .views import index, contacto , produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contacto),
    path('produto/<int:pk>', produto, name='produto'),
]

