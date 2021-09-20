from django.contrib import admin
# from django.contrib.admin.decorators import display
from django.db import models
from .models import category, foodArgus

@admin.register(foodArgus)
class foodArgusAdmin(admin.ModelAdmin):
    list_display = ('name',  'rate' , 'auth', 'categ_to_str')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('desc',)

    def categ_to_str(self, obj):
        return ", ".join([category.name for category in obj.showornot()])
    categ_to_str.short_description ='دسته‌بندی'


@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name','check', 'parent')
    prepopulated_fields = {'theslg': ('name',)}

# Register your models here.