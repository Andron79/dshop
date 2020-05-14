from django.contrib.auth import views
from django.urls import path
# from accounts import views

from django.urls import path


app_name = 'accounts'


urlpatterns = [

    path('login/', views.LoginView.as_view(), name='login'),
    # path('signup/', views.signup, name='signup'),

]