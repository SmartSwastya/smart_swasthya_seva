from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Direct view to render home page (index.html)
def home(request):
    return render(request, 'index.html')  # Make sure 'index.html' is in your templates folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_panel/', include('admin_panel.urls')),
    path('doctor/', include('doctor.urls')),
    path('patient/', include('patient.urls')),
    # Remove the service app path if it's not needed
    # path('service/', include('service.urls')),  # Remove this line
    path('', home, name='home'),  # Home page route directly
]
