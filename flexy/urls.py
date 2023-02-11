from django.urls import path
from flexy import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('addrecharge/', views.addrecharge, name='addrecharge'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout'),
]
