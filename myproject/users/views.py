# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)  # Data from POST request
        if form.is_valid():  # Check if form is valid
            user = form.save()
            login(request, user)  # Logowanie użytkownika
            messages.success(request, "Rejestracja zakończona sukcesem.")  # View message
            return redirect("/")
        else:
            messages.error(request, "Błąd rejestracji.")  # View message
    else:
        form = CustomUserCreationForm()  # Create empty form
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)  # Data from POST request
        if form.is_valid():
            user = form.get_user()  # Get user from form
            login(request, user)
            messages.success(request, "Pomyślnie zalogowano.")
            if "next" in request.POST:
                return redirect(request.POST.get("next"))  # Redirect to next page if exists
            else:
                return redirect("/")
        else:
            messages.error(request, "Błąd logowania.")
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Pomyślnie wylogowano.")
        return redirect("/")
