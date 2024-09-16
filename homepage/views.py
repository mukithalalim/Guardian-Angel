from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import SignUpForm


def home(request):
    """
    This method will load the homepage

	:param name: request - used to generate responses(Http) depending on the request that it receives.
	:param type: HttpResponse
	:return: returns the homepage
	"""
    return render(request, 'homepage/home.html')


def index(request):
    """
    This method will load the index page

	:param name: request - used to generate responses(Http) depending on the request that it receives.
	:param type: HttpResponse
	:return: returns the index page
	"""
    return render(request, 'homepage/index.html')


def login_page(request):
    """
    This method will load the login page and take the required information to log in.
    If the user is already authenticated then it will redirect the user to homepage.
    Else, it will take the required information to authenticate.
    If the infromation is right then it will redirect the user to homepage.
    If the infromation is worng then it will give an error message and ask for the username and password again.

	:param name: request - used to generate responses(Http) depending on the request that it receives.
	:param type: HttpResponse
	:return: returns the homepage if authenticated else, ask for information to login.
	"""
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect')
                return render(request, 'homepage/login.html')

        return render(request, 'homepage/login.html')


def logout_page(request):
    """
    This method will execute the logout page and redirect the user to login page.
    
	:param name: request - used to generate responses(Http) depending on the request that it receives.
	:param type: HttpResponse
	:return: returns the login page.
	"""
    logout(request)
    return redirect('login')


def register(request):
    """
    This method will load the registration page and take the required information to register as a new user.
    If the user is already authenticated then it will redirect the user to homepage.
    Else, it will take the required information to register.
    If the infromation is right then it will redirect the user to login with a message.
    If the infromation is worng then it will ask for the proper information again.

	:param name: request - used to generate responses(Http) depending on the request that it receives.
	:param type: HttpResponse
	:return: returns the homepage if authenticated else, ask for information to register.
	"""
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = SignUpForm()

        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Welcome ' + user + ', you can login now')
                return redirect('login')

        context = {'form': form}
        return render(request, 'homepage/registration.html', context)

