from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'), 
    path('delete-task/', views.DeleteTask, name='delete'),
    path('update/', views.Update, name='update'),
]