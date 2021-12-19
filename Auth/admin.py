from django.contrib import admin
from .models import List, user_ip

# Register your models here.
admin.site.register(List)
admin.site.register(user_ip)