from django.contrib import admin
from blog.models import *
# Register your models here.
@admin.register(Posts)
class adminPost(admin.ModelAdmin):
    list_display = ('title','created_time','modified_time','category',)
@admin.register(Category)
class adminCategory(admin.ModelAdmin):
    list_display = ('name',)
admin.register(adminPost)
admin.register(adminCategory)