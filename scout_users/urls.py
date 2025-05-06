from django.urls import path
from . import views

urlpatterns = [
    path('signup/customer/', views.CustomerSignupView.as_view(), name='customer-signup'),
    path('signup/service-provider/', views.ServiceProviderSignupView.as_view(), name='service-provider-signup'),
    path('user-detail/', views.UserDetailAPIView.as_view(), name='user-detail'),
    path('update/customer/', views.CustomerUserUpdateView.as_view(), name='customer-update'),
    path('update/service-provider/', views.ServiceProviderUserUpdateView.as_view(), name='service-provider-update'),
]
