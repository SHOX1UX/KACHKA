from django.contrib import admin
from .models import Contact, Trainer
# Register your models here.

admin.site.register((Trainer,Contact))