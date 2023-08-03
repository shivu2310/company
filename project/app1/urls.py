from django.urls import path
from app1 import views

urlpatterns = [
     path('', views.home, name='home'),
     path('login/', views.loginpage, name='login'),
     path('about/', views.about , name='about'),
     path('signcos/', views.signcos, name='signcos'),
     path('stusign/', views.stusign, name='stusign'),
     path('myprofile/',views.profile , name='myprofile'),
     path('logout/' , views.logoutPage , name='logout' ),
     path('postpage/' , views.postPage , name='postpage' ),
     path('contact/' , views.contact , name='contact' ),
     path('service/' , views.service , name='service' ),
]
