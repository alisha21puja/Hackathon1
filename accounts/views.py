
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.urls import path, include
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Article, UserProfile
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import ArticleForm


def loginn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            key = user._get_pk_val()
            user_1 = list(UserProfile.objects.values_list(
                'type_usr', 'id').filter(id=key).values('type_usr'))
            user_type = user_1[0]
            var = user_type['type_usr']

            if user_type['type_usr'] == 100:
                auth.login(request, user)
                request.session['userid'] = key
                return redirect('participantIndex')
                # return redirect('participantIndex')
            elif user_type['type_usr'] == 200:
                auth.login(request, user)
                request.session['userid'] = key
                return redirect('sponsorIndex')
            elif user_type['type_usr'] == 300:
                auth.login(request, user)
                request.session['userid'] = key
                return redirect('organiserIndex')
            else:
                messages.error(
                    request, 'invalid user type dectected contact admin')
                return render(request, 'login.html', {'error': 'invalid user type dectected contact admin'})
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, ' You are now loged out')
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirmpassword']
        phone = request.POST['phone']
        type_usr = request.POST['type_usr']
        src = request.POST['profile_img']
        #mobile  = request.POST['mobile']
        #userType = request.POST['usertype']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is taken")
                return render(request, 'login.html', {'errorr': 'Username is already taken'})
                # return redirect('accounts')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is been use")
                    return render(request, 'login.html', {'errorr': 'Email is in use '+email})
                    return redirect('accounts')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # auth.login(request,user)
                    #messages.success(request,'You are now Loged in')
                    user.save()
                    key = user._get_pk_val()
                    var = UserProfile(id=key, type_usr=type_usr,
                                      phone=phone, profile_img=src)
                    var.save()
                    message = ""
                    if type_usr == 100:
                        message = "User Name :"+email + " PASSWORD :" + password + \
                            " EMAIL : "+email+" PHONE : "+phone+" Role : PARTICIPANT"
                    elif type_usr == 200:
                        message = "User Name :"+email + " PASSWORD :" + password + \
                            " EMAIL : "+email+" PHONE : "+phone+" Role : SPONSER"
                    elif type_usr == 300:
                        message = "User Name :"+email + " PASSWORD :" + password + \
                            " EMAIL : "+email+" PHONE : "+phone+" Role : ORGANISER"

                    send_mail('Subject' + "YOU HAVE NOW REGISTERED TO TECH EVENT",
                              'Message' + message + 'Will Contact your soon',
                              'sachin.thakur9614@gmail.com',
                              [email, 'sachin.thakur@mca.christuniversity.in', ],
                              fail_silently=True)
                    messages.success(request, 'You are now registered in')
                    return redirect('accounts')
        elif first_name == '':
            messages.error(request, 'FirstName  field  is empty')
        elif last_name == '':
            messages.error(request, 'Last Name field  is empty')
        elif username == '':
            messages.error(request, 'Username field  is empty')
        elif email == '':
            messages.error(request, 'Email field   is empty')
        elif password == '':
            messages.error(request, 'Password is empty')
        elif password2 == '':
            messages.error(request, 'Confirm password field is empty')
        else:
            messages.error(request, 'Password do not match')
            return redirect('accounts')
    else:
        return render(request, 'base.html')


def indx(request):
    return render(request, 'login.html')
