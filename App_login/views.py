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
        name = request.data['full_name']
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




