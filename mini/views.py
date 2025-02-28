from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name='home/index.html')

def about(request):
    return render(request, template_name='home/about.html')

def category(request):
    return render(request,'home/category.html')

def portfolio(request):
    return render(request, template_name='home/portfolio.html')

def blog(request):
    return render(request, template_name='home/blog.html')

def contact(request):
    return render(request, template_name='home/contact.html')

def login(request):
    return render(request, template_name='home/login.html')

def register(request):
    return render(request, template_name='home/register.html')
