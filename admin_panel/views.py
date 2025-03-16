from django.shortcuts import render

def index(request):
    return render(request, 'admin_panel/admin_panel.html')  # Make sure this template exists
