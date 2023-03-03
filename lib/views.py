from django.shortcuts import render,get_object_or_404,redirect
from .models import book
from .forms import BookForm

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
    if request.method =='POST':
        form =BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BookForm()
    return render(request,'registration.html',{'form':form})
def authordetail(request,pk):
    bookk=get_object_or_404(book,pk=pk)
    return render(request,'authordetail.html',{'book':bookk})
