from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from django.utils import timezone
# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    images = Image.objects.all()
    user = request.user.username
    context = {'images': images, 'user': user}
    return render(request, 'index.html', context)


@login_required
def add(request): 
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
 
        if form.is_valid():
            form = form.save(commit=False)
            form.dateAdded = timezone.now()
            form.user = request.user
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'add.html', {'form': form})
 

def success(request):
    return render(request, 'success.html')