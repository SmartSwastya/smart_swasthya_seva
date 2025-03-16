### admin.py
from django.contrib import admin
from .models import HomeModel

@admin.register(HomeModel)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)