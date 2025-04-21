from django.shortcuts import render
from scout_users.models import User, Customer,ServiceProvider
from scout_users.serializers import UserSerializer
from scout_users.SignupSerializer import CustomerSignupSerializer, ServiceProviderSignupSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model                                                          
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response

# Create your views here.

# views.py


class CustomerSignupView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSignupSerializer


class ServiceProviderSignupView(generics.CreateAPIView):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSignupSerializer
class UserDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve user details.
    Only accessible to authenticated users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# class UserDetailAPIView(generics.RetrieveAPIView):
#     """
#     API view to retrieve user details.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user
