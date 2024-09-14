from django.shortcuts import render, redirect

# Create your views here.

#to add new user with django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignupForm

def signup(request):
    form=SignupForm()
    if request.method == 'POST':
        form=SignupForm(request.POST)  #resive data from the form
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('home')
    return render(request, 'signup.html',{'form':form})
