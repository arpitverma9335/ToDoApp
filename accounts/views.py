from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from todoapp.models import *
import datetime as dt
from django.core.mail import send_mail
from django.conf import settings
import random
# Create your views here.

def register_func(request):
      if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            #address = request.POST['address']
            
            pass1 = request.POST['Password1']
            pass2 = request.POST['Password2']

            if pass1 == pass2:
                  if User.objects.filter(username=username).exists():
                        messages.info(request,'username taken')
                        return render(request,'register.html')
                  elif User.objects.filter(email=email).exists():
                        messages.info(request,'Email already taken')
                        return render(request,'register.html')
                  else:
                        user = User.objects.create_user(username = username , password = pass1 , email = email , first_name = first_name , last_name = last_name)
                        user.save()
                        string = ''
                        for i in range(3):
                              string += str(random.randrange(11,99))
                        c = int(string)
                        get_code_by_mail(user.email , user.first_name , c)
                        veri = code(user = user , code = c)
                        veri.save()
                        return redirect('verify/')
            else:
                  messages.info(request,"password mismatch")
                  return render(request,'register.html')
      
      else:
            return render(request , 'register.html')

def login_func(request):
      if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username , password = password)

            if user is not None:
                  obj = code.objects.filter(user = user)
                  if len(obj) != 0:
                        if obj[0].is_verified:
                              auth.login(request , user)
                              return redirect('/')
                        else:
                              return redirect('verify/')
                  else:
                        string = ''
                        for i in range(3):
                              string += str(random.randrange(11,99))
                        c = int(string)
                        obj = code(user = user , code = c)
                        obj.save()
                        get_code_by_mail(user.email,user.first_name ,  c)
                        return redirect('verify/')
            else:
                  messages.info(request , 'Invalid Username or Password')
                  return render(request,'login.html')
      else:
            return render(request , 'login.html')

def logout_func(request):
      auth.logout(request)
      return redirect('/')

def my_account(request):
      user = User.objects.all()
      return render(request , 'myaccount.html')

def update_details(request):
      try:
            if request.method == 'POST':
                  user_id = request.user.id
                  email = request.POST['email']
                  mobile_no = request.POST['mobile_no']
                  profile = profile_user(email = email , mobile_no = mobile_no , user_id = user_id)
                  profile.save()
                  return redirect('/')
            else:
                  return render(request , 'mydetails.html')
      except Exception as e:
            user_id = request.user.id
            u = profile_user.objects.get(user_id = user_id)
            u.delete()
            if request.method == 'POST':
                  user_id = request.user.id
                  email = request.POST['email']
                  mobile_no = request.POST['mobile_no']
                  profile = profile_user(email = email , mobile_no = mobile_no , user_id = user_id)
                  profile.save()
                  return redirect('/')
            else:
                  return render(request , 'mydetails.html')

def my_details(request):
      user = User.objects.all()
      return render(request , 'profile.html')


def your_account(request):
      return render(request , 'accounts.html')
       
def List_func(request):
      user_id = request.user.id
      if request.method == 'POST':
            item = request.POST['task']
            completed = request.POST['completed']
            date = request.POST['date']
            listy = List(item = item , user_id = user_id , completed = completed , date = date)
            listy.save()
            return redirect('/')
      else:
            return render(request,'input_element.html')


def get_code_by_mail(email ,name ,  code):
      subject = "regularly.herokuapp.com"
      message = f'Hi {name} , {code} is your 6 digit code to verify this email!'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [email,]
      send_mail(subject , message , email_from , recipient_list)

def verify(request):
      return render(request , 'verify.html')

def verify_token(request):
      v_code = request.POST.get('code')
      username = request.POST.get('username')
      obj1 = User.objects.filter(username = username)
      for i in obj1:
            user_id = i.id
      obj2 = code.objects.filter(user_id = user_id)
      for i in obj2:
            if int(i.code) == int(v_code):
                  obj2[0].is_verified = True
                  obj2[0].save()
                  messages.info(request , 'Your account has been verified \n Login to continue')
            else:
                  return render(request , 'error.html')
      return redirect('/accounts/login')




      
