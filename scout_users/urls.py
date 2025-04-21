from django.urls import path
from . import views

urlpatterns = [
    # path('<uuid:user_uuid>', views.UserDetailAPIView.as_view(), name='user-detail'),  
    path('signup/customer/', views.CustomerSignupView.as_view(), name='customer-signup'),
    path('signup/service-provider/', views.ServiceProviderSignupView.as_view(), name='service-provider-signup'),
    path('<uuid:user_uuid>', views.UserDetailAPIView.as_view(), name='user-detail'),

]
