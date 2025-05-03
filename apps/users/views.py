from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse


def test_manual_login(request):
    user = authenticate(request, username='Шахмир', password='Shax3127457')
    if user is not None:
        login(request, user)
        return HttpResponse(f"Успешно: {user.username}")
    else:
        return HttpResponse("Не удалось авторизоваться")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("catalog:category_list")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("catalog:category_list")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("catalog:category_list")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # сразу логиним
            return redirect("catalog:category_list")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("users:login")



@login_required
def profile_panel(request):
    return render(request, 'users/profile_panel.html', {'user_obj': request.user})
