from django.contrib import admin
from .models import CustomUser, AdminUpload
# Register your models here.

admin.site.register((CustomUser, AdminUpload))