from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='doctor_home'),  # Doctor homepage
]
