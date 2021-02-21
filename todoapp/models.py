from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
# Create your models here.
class profile_user(models.Model):
      user = models.OneToOneField(User , on_delete = models.CASCADE)
      email = models.EmailField()
      mobile_no = models.CharField(max_length = 12)
      def __str__(self):
            return f'{self.user.username} profile_user'
class List(models.Model):
      user = models.ForeignKey(User , on_delete = models.CASCADE)
      item = models.CharField(max_length = 150)
      completed = models.BooleanField(default = False)
      date=models.DateTimeField(default=timezone.now)

class user_ip(models.Model):
      ip = models.GenericIPAddressField(default = None)
      time = models.DateField(default=timezone.now)

class code(models.Model):
      user = models.OneToOneField(User , on_delete = models.CASCADE)
      code = models.IntegerField()
      is_verified = models.BooleanField(default=False)

      def __str__(self):
            return self.user.username
