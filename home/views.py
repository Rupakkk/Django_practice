from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Subject=request.POST['subject']
        Message=request.POST['message']
        data=Contact.objects.create(
            name=Name,
            email=Email,
            subject=Subject,
            message=Message
        )
    return render(request,'contact.html')

def post(request):
    return render(request,'post.html')
