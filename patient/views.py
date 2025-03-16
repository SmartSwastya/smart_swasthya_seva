from django.shortcuts import render

def index(request):
    return render(request, 'patient/patient.html')  # Make sure this template exists
