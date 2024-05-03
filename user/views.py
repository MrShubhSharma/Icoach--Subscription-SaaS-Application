from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/course")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})



def logout_view(request):
    logout(request)
    return redirect("login")