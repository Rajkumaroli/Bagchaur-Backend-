from django.shortcuts import render, HttpResponse
from .models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method=='POST':
        name = request.POST["name"]
        email = request.POST["email"]
        comment = request.POST["comment"]
        data = Contact.objects.create(name=name,email=email,comment=comment)
        data.save()
    return render(request, 'contact.html')