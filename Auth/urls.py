from django.urls import path , re_path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
      path('', views.indexFunc),
      path('input-task',views.listInput),
      path('delete-task',views.itemDelete),
      path('profile', views.profileFunc),
               ]

