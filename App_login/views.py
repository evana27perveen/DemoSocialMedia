from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

# Internal Imports
from App_main.models import *
from App_main.serializers import *
from App_login.models import *
from App_login.serializers import *


# Create your views here.
@api_view(['POST'])
def registerAPIView(request):
    if request.method == 'POST':
        name = request.data['name']
        email = request.data['email']
        password = request.data['password']
        password2 = request.data['password2']
        user = CustomUser(email=email)
        if password == password2:
            user.set_password(password)
            user.save()
            profile_ = Profile(user=user, full_name=name)
            profile_.save()
            return Response({"Success": "Successfully registered!!!"})
        else:
            return Response({"Error": "Password is not matched!!!"})


@api_view(['POST'])
def otp_checker(request):
    if request.method == 'POST':
        OTP = request.data['otp']
        myOTP = OTPModel.objects.get(user=request.user)
        if OTP == myOTP.otp:
            otp = f"{request.user.id}-{random.randint(100000,999999)}"
            myOTP.otp = otp
            myOTP.save()
            return Response({"Success": "Correct OTP"})
        else:
            return Response({"Wrong": "Incorrect OTP"})