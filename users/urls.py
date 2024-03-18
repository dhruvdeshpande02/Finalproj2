from django.urls import path
from . import views

urlpatterns = [
    path('all-students/', views.all_students, name='all_students'),
    path('register-student/', views.register_student, name='register-student'),
    path('register-coordinator/', views.register_coordinator, name='register-coordinator'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


    

]
