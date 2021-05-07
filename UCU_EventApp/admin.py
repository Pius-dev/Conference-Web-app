from django.contrib import admin

# Register your models here.
from . import models
from . models import Member,Contact


admin.site.register(models.Member)



admin.site.register(models.Contact)



