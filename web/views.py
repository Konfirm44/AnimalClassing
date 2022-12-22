from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    images = Image.objects.filter(user=request.user)
    #user = request.user.username
    context = {'images': images}
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


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/success")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserCreationForm()
    return render (request, 'registration/register.html', {"register_form":form})