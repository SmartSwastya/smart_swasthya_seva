from django.contrib import admin
from .models import AdminUser  # Import your model

admin.site.register(AdminUser)  # Register the model to admin
