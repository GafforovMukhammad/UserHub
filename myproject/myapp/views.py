from django.shortcuts import render
from .models import User

def index(request):
    users = User.objects.all()  # Fetch all user records
    context = {'users': users}
    return render(request, 'myapp/index.html', context)
