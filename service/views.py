from django.shortcuts import render

def index(request):
    return render(request, 'service/service.html')  # Make sure this template exists
