from django.shortcuts import render
from . import views
from .models import Staff
# Create your views here.
def index (request):
    staffs=Staff.objects.all
    return render(request,"index.html",{'staffs':staffs})