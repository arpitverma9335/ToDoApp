from django.contrib import admin
from .models import profile_user
from .models import List
from .models import user_ip
from .models import code

# Register your models here.
admin.site.register(profile_user)
admin.site.register(List)
admin.site.register(user_ip)
admin.site.register(code)