from django.shortcuts import render
from .models import book

# Create your views here.
def home(request):
    Book=book.objects.all()
    context={"books":Book}
    return render(request,'index.html', context)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def registration(request):
    return render(request,'registration.html ')
def authordetail(request):
    return render(request,'authordetail.html')