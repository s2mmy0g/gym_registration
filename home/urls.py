from django.urls import path
from home import views
urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('s404',views.s404),
    path('about_us',views.about_us),
    path('blog',views.blog),
    path('blog_details',views.blog_details),
    path('bmi_calculator',views.bmi_calculator),
    path('class_details',views.class_details),
    path('class_timetable',views.class_timetable),
    path('contact',views.contact),
    path('gallery',views.gallery),
    path('services',views.services),
    path('team',views.team),
]