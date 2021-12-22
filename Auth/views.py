from django.shortcuts import render, redirect
from .models import List, user_ip
from django.contrib.auth.models import User, auth
import datetime as dtm
from django.utils import timezone
from datetime import datetime
from django.db.models import Count
import pytz
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect,redirect

def indexFunc(request):
      x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
      if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
      else:
            ip = request.META.get('REMOTE_ADDR')
      u = user_ip(ip = ip)
      if len(user_ip.objects.filter(ip = ip).values()) > 0:
            pass
      else:
            u.save()
      group = user_ip.objects.values('time').annotate(dcount=Count('ip')).order_by('-time')
      date_list , count_list = [] , []
      if len(group) <= 7:
            length = len(group)
      else:
            length = 7
      for ele in range(0 , length):
            date_list.append(group[ele]['time'].strftime('%Y-%m-%d'))
            count_list.append(group[ele]['dcount'])
      current_id = request.user.id
      activities_1= List.objects.filter(user__id=current_id , completed='True').order_by('date').values()
      activities_2 = List.objects.filter(user__id=current_id , completed='False').order_by('date').values()
      time_rem_1 , time_rem_2 = [] , []
      dt_now = datetime.now(tz=pytz.timezone('Asia/Kolkata'))
      print('####', dt_now)
      for i in activities_1:
            dt_due = i.get('date')
            t_left = (dt_due - dt_now).total_seconds()
            if t_left < 0:
                  time_rem_1.append('Time is Up')
                  continue
            days = int(t_left/(3600 * 24))
            hrs = int((t_left % (3600 * 24))/3600)
            time_rem_1.append(f'{days} days, {hrs} hours')
      for i in activities_2:
            dt_due = i.get('date')
            t_left = (dt_due - dt_now).total_seconds()
            if t_left < 0:
                  time_rem_2.append('Time is Up')
                  continue
            days = t_left//(3600 * 24)
            hrs = (t_left % (3600 * 24))//24
            time_rem_2.append(f'{days} days, {hrs} hours')
      return render(request,'index.html',{'date':date_list[-1::-1] , 'count':count_list[-1::-1] , 'activities_crit':zip(activities_1 , time_rem_1) , 'activities_ncrit':zip(activities_2 , time_rem_2)})

def listInput(request):
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

def itemDelete(request):
      if request.method == 'GET':
            act_id = request.GET['act_id']
            obj = get_object_or_404(List,id = act_id)
            obj.delete()
            return HttpResponseRedirect("/")
      else:
            return render(request,'index.html')

def itemUpdate(request):
      if request.method == 'GET':
            act_id = request.GET['act_id']
            obj = get_object_or_404(List,id = act_id)
            return render(request,'update.html', {'obj':obj})
      elif request.method == 'POST':
            act_id = request.POST['act_id']
            item = request.POST['task']
            completed = request.POST['completed']
            date = request.POST['date']
            obj = get_object_or_404(List,id = act_id)
            obj.item = item
            obj.completed = completed
            obj.date = date
            obj.save()
            return redirect('/')
      else:
            return render(request,'index.html')

def profileFunc(request):
      user = User.objects.all()
      return render(request , 'myaccount.html')