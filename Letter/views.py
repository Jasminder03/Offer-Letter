from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import registrationFrom
from .models import registration,Image,Image2

def home(request):
    submitted = False
    if request.method == "POST":
        form = registrationFrom(request.POST)
        if form.is_valid():
            form.save()
            registrationdata = registration.objects.last()
            imagedata = Image.objects.all()
            image2data = Image2.objects.all()
            data = {
                'registrationdata' : registrationdata,
                'imagedata' : imagedata,
                'image2data' : image2data
            }
            return render(request, 'letter/letter.html',data)
    else:
        form=registrationFrom
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'letter/index.html', {'form': form ,'submitted': submitted})

def letter(request):
    return render(request, 'letter/letter.html')