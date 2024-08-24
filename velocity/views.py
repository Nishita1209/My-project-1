from django.shortcuts import render,redirect
from velocity.models import Velocity
from velocity.forms import VelocityForm
def home(request):
    return render(request,'home.html')

def contact(request):
    velocityform=VelocityForm(request.POST or None)
    if velocityform.is_valid():
        velocityform.save()
        return redirect('home')

    return render(request,'contact.html',{"forms":velocityform})
