from django.shortcuts import render

def index(request):
    return render(request, 'doctor/doctor.html')  # Make sure this template exists
