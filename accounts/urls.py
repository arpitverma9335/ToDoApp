from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import password_reset , password_reset_done

urlpatterns = [
      path('register_form',views.register_func),
      path('login' , views.login_func),
      path('logout' , views.logout_func),
      path('your_account' , views.your_account),
      path('my_account' , views.my_account),
      path('verify/' , views.verify),
      path('verify/token',views.verify_token),
      #path('profile.com' , views.my_profile),
      #path('gallery' , views.my_gallery),
      path('UpdateDetails_form',views.update_details),
      path('MyDetails',views.my_details),
      path('input_task',views.List_func),
      #path('update_profile',views.update_func),
      path('reset_password/', auth_views.PasswordResetView.as_view() , name = 'reset_password'),
      path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view() , name = 'password_reset_done'),
      path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
      path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "passwordcomplete.html") , name = 'password_reset_complete'),
      #path('comments.com' , views.comments_func),
      #path('all_comments.com' , views.all_comments_func), 
               ]    # path cvonnects form 'xyz.com' with add() in views

