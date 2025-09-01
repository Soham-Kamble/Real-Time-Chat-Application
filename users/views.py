from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth import login

# Register view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # or your home page
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Custom login view
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = '/rooms/'


# Custom logout view
class CustomLogoutView(LogoutView):
    next_page = 'login' 
