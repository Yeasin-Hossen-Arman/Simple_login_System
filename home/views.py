from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

# Create your views here.

def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact= Contact(name = name, email = email, phone = phone, desc = desc)
        contact.save()
    return render(request, "index.html")
    # return HttpResponse("home page")
