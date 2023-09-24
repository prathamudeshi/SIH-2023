from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('upload_document/', views.upload_document, name = "upload_document"),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('getDocuments/<str:room>/', views.getDocuments, name='getDocuments'),
]