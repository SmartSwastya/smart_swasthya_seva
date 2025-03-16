from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='service_home'),  # Service homepage
]
