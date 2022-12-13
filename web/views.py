from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from django.utils import timezone
# Create your views here.

from django.http import HttpResponse


def index(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'index.html', context)

    
def add(request): 
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
 
        if form.is_valid():
            form = form.save(commit=False)
            form.dateAdded = timezone.now()
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'add.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')