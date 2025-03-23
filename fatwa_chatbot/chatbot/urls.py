from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),
    path('getResponse',views.getResponse, name='getResponse') # it's about to send data from FrontEnd -> BackEnd
]