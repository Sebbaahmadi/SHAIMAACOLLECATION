from django.shortcuts import render
from.models import Contact
from django.http import HttpResponse
# Create your views here.
def contact (request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        contact.name = name
        contact.email = email
        contact.massage = massage
        contact.save()
        return HttpResponse("<h1>Thanks For Contact Me<h1>")

    return render(request, 'contact/contact.html')

