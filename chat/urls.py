from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),  
    path('<str:room>/',view.room, name='room')
]
