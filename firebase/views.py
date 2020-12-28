import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from requests import request
from django.contrib.auth.decorators import login_required


def login_firebase(request):
    return render(request, 'login.html')



def home(request):

    if request.user.is_authenticated:
        return redirect('user:profile')
    else:
        return render(request, 'login.html')


@csrf_exempt
def login_firebase_save(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    provider = request.POST.get("provider")
    token = request.POST.get("token")
    firbase_response = loadDatafromFirebaseApi(token)
    firbase_dict = json.loads(firbase_response)

    if "users" in firbase_dict:
        user = firbase_dict["users"]
        if len(user) > 0:
            user_one = user[0]
            if "phoneNumber" in user_one:
                if user_one["phoneNumber"] == email:
                    data = proceedToLogin(request, email, username, token, provider)
                    return HttpResponse(data)
                else:
                    return HttpResponse("Invalid Login Request")
            else:
                if email == user_one["email"]:
                    provider1 = user_one["providerUserInfo"][0]["providerId"]
                    if user_one["emailVerified"] == 1 or user_one["emailVerified"] == True or user_one[
                        "emailVerified"] == "True" or provider1 == "facebook.com":
                        data = proceedToLogin(request, email, username, token, provider)
                        return HttpResponse(data)
                    else:
                        return HttpResponse("Please Verify Your Email to Get Login")
                else:
                    return HttpResponse("Unknown Email User")
        else:
            return HttpResponse("Invalid Request User Not Found")
    else:
        return HttpResponse("Bad Request")

def loadDatafromFirebaseApi(token):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:lookup"

    payload = 'key=AIzaSyDbl81jCjoxxH3EQSt8-z37QmRZlfYJe7c&idToken='+token
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = request("POST", url, headers=headers, data=payload)

    return response.text


def proceedToLogin(request,email,username,token,provider):
    users=User.objects.filter(username=username).exists()

    if users==True:
        user_one=User.objects.get(username=username)
        user_one.backend='django.contrib.auth.backends.ModelBackend'
        login(request,user_one)
        return "login_success"
    else:
        user=User.objects.create_user(username=username,email=email,password=settings.SECRET_KEY)
        user_one=User.objects.get(username=username)
        user_one.backend='django.contrib.auth.backends.ModelBackend'
        login(request,user_one)
        return "login_success"


def login_request(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'success': 200})
    else:
        return JsonResponse({'error': 500})
