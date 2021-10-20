from django.urls import path
from Login_app import views
app_name = 'Login_app'

urlpatterns = [
    path('signup/', views.Sign_up, name='Sign_up'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('profile/', views.Profile_page, name='Profile_page'),
    path('change/', views.change_user, name='change_user'),
    path('password/', views.pass_change, name='password'),
    path('addprofile_pic/', views.add_profile_pic, name='add_profile_pic'),
    path('change_pro_pic/', views.change_pro_pi, name='change_pro_pi'),
]
