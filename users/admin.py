from django.contrib import admin
from . models import Profile
from django.contrib.admin.options import ModelAdmin
class ProfileAdmin(ModelAdmin):
    list_display = ["image", "resume"]

admin.site.register(Profile,ProfileAdmin)
