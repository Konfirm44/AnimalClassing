from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def logIn(request):
    if request.user.is_authenticated:
        return redirect('')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is not None:
                login(request, user)
                return redirect('')
            else:
                context = {'form': form}
                return render(request, 'login.html', context)   
        else:
            context = {'form': form}
            return render(request, 'login.html', context)
    else:    
        context = {'form': LoginForm()}
        return render(request, 'login.html', context)


def logOut(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')