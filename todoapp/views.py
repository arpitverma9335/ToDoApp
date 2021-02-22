#from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect,redirect
from django.contrib import messages
from .models import List , user_ip
import datetime as dtm
from datetime import datetime , timezone
from django.db.models import Count
import pytz

# Create your views here.
def index_func(request):
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
      for ele in range(0 , 7):
            date_list.append(group[ele]['time'].strftime('%Y-%m-%d'))
            count_list.append(group[ele]['dcount'])
      current_id = request.user.id
      activities_1= List.objects.filter(user__id=current_id , completed='True').order_by('date').values()
      activities_2 = List.objects.filter(user__id=current_id , completed='False').order_by('date').values()
      time_rem_1 , time_rem_2 = [] , []
      for i in activities_1:
            dt_now = datetime.now(tz=pytz.timezone('ASia/Kolkata'))
            dt_due = i.get('date')
            t_left = dt_due - dt_now
            if (t_left).total_seconds() < 0:
                  time_rem_1.append('Time is Up')
                  continue
            time_rem_1.append(t_left)
      for i in activities_2:
            dt_now = datetime.now(tz=pytz.timezone('ASia/Kolkata'))
            dt_due = i.get('date')
            t_left = dt_due - dt_now
            if (t_left).total_seconds() < 0:
                  time_rem_2.append('Time is Up')
                  continue
            time_rem_2.append(t_left)
      return render(request,'index.html',{'date':date_list[-1::-1] , 'count':count_list[-1::-1] , 'activities_crit':zip(activities_1 , time_rem_1) , 'activities_ncrit':zip(activities_2 , time_rem_2)})

def contact_func(request):
      email = 'asme.arpitverma19@gmail.com'
      return render(request,'contact.html',{'email':email})
      
def remove_func(request):
      if request.method == 'GET':
            act_id = request.GET['act_id']
            obj = get_object_or_404(List,id = act_id)
            obj.delete()
            return HttpResponseRedirect("/")
      else:
            return render(request,'index.html')
