from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'index.html')
    
def about(request):
    return render(request , 'about.html')
    
def contact(request):
    return render(request , 'contact.html')

def viewMore1(request):
    return render(request , 'viewMore1.html')
    
def viewMore2(request):
    return render(request , 'viewMore2.html')