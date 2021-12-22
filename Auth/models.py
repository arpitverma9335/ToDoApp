from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

class List(models.Model):
      user = models.ForeignKey(User , on_delete = models.CASCADE)
      item = models.CharField(max_length = 150)
      completed = models.BooleanField(default = False)
      date=models.DateTimeField(default=timezone.now)

      def __str__(self):
            return self.user.first_name

class user_ip(models.Model):
      ip = models.GenericIPAddressField(default = None)
      time = models.DateField(default=timezone.now)

      def __str__(self):
            return f'{self.ip}_{self.time}'