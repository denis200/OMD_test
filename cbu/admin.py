from django.contrib import admin
from .models import UserTable, CBUData


@admin.register(UserTable)
class BlogAdmin(admin.ModelAdmin):
    list_display =('id','user')


@admin.register(CBUData)
class BlogAdmin(admin.ModelAdmin):
    list_display =('id','user_table','unit', 'reach')