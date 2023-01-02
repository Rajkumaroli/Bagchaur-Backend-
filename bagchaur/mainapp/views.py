from django.shortcuts import render, HttpResponse, redirect
from .models import Contact, Janpratinidhi, Staff, Ward1, Ward2, Ward3, Ward4, Ward5, Ward6, Ward7, Ward8, Ward9, Ward10, Ward11, Ward12
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method=='POST':
        name = request.POST["name"]
        email = request.POST["email"]
        comment = request.POST["comment"]
        if len(name)<2 or len(email)<3 or len(comment)<2:
            messages.error(request, "All field is Required!!")
        else:
            data = Contact.objects.create(name=name,email=email,comment=comment)
            data.save()
            messages.success(request, "Thanks for contacting us! We will be in touch with you shortly.")
    return render(request, 'contact.html')

def introduction(request):
    return render(request, 'introduction.html')

def janpratinidhi(request):
    infos = Janpratinidhi.objects.all()
    return render(request, 'janpratinidhi.html', {'infos':infos})

def staff(request):
    staffs = Staff.objects.all()
    return render(request, 'staff.html', {'staffs':staffs})

def ward1(request):
    wards1 = Ward1.objects.all()
    return render(request, 'ward1.html', {'wards1':wards1})

def ward2(request):
    wards2 = Ward2.objects.all()
    return render(request, 'ward2.html', {'wards2':wards2})

def ward3(request):
    wards3 = Ward3.objects.all()
    return render(request, 'ward3.html', {'wards3':wards3})

def ward4(request):
    wards4 = Ward4.objects.all()
    return render(request, 'ward4.html', {'wards4':wards4})

def ward5(request):
    wards5 = Ward5.objects.all()
    return render(request, 'ward5.html', {'wards5':wards5})

def ward6(request):
    wards6 = Ward6.objects.all()
    return render(request, 'ward6.html', {'wards6':wards6})

def ward7(request):
    wards7 = Ward7.objects.all()
    return render(request, 'ward7.html', {'wards7':wards7})

def ward8(request):
    wards8 = Ward8.objects.all()
    return render(request, 'ward8.html', {'wards8':wards8})

def ward9(request):
    wards9 = Ward9.objects.all()
    return render(request, 'ward9.html', {'wards9':wards9})

def ward10(request):
    wards10 = Ward10.objects.all()
    return render(request, 'ward10.html', {'wards10':wards10})

def ward11(request):
    wards11 = Ward11.objects.all()
    return render(request, 'ward11.html', {'wards11':wards11})

def ward12(request):
    wards12 = Ward12.objects.all()
    return render(request, 'ward12.html', {'wards12':wards12})

def municipalD(request):
    return render(request, 'municipalD.html')