from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

from tickets.models import Ticket




# Create your views here.

@login_required
def index(request):
    request.session.set_test_cookie()
    user = User.objects.get(username=request.user.username)
    visitor_cookie_handler(request)
    context_dict = {}
    context_dict['visits'] = request.session['visits']
    return render(request, 'connect/index.html', context=context_dict)


def landing(request):
    """The landing page view that anonymous users see
    when they arrive to the website"""
    return render(request, "connect/landing.html")


def user_login(request):
    """The login view that enables users to login to the platform """
    authenticated = False
    login_form = LoginForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) # authenticate user
        if user:
            if user.is_active:
                login(request, user)
                authenticated = True
                return redirect('index')
            else:
                print(login_form.errors)
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
    else:
        login_form = LoginForm()

    return render(request, 'connect/login.html',
                  {'login_form': login_form, 'authenticated': authenticated})


@login_required
def user_logout(request):
    """The user logout view"""
    logout(request)
    return HttpResponseRedirect('/tickets/')


# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
    """Function to retrieve the server side cookie"""
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val



def visitor_cookie_handler(request):
    """The cookie handler view"""
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                                str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    # If it's been more than a day since the last visit
    # update the last visit cookie now that we have updated the count
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1
        # set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits