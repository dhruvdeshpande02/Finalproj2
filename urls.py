from django.urls import path
from . import views

urlpatterns = [
    path('all-students/', views.all_students, name='all_students'),
    path('all-coordinators/', views.all_coordinators, name='all_coordinators'),
    path('register-student/', views.register_student, name='register-student'),
    path('register-coordinator/', views.register_coordinator, name='register-coordinator'),
    path('register-tnpoffice/', views.register_tnpoffice, name='register-tnpoffice'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

   path('apply-drive/<int:drive_id>/', views.apply_drive, name='apply_drive'),
    path('application/success/', views.application_success, name='application_success'),
    path('drive/application/exists/', views.drive_application_exists, name='drive_application_exists'),
    path('drive/applied_students/<int:drive_id>/', views.applied_students_for_drive, name='drive_applied_students'),
    path('my_applied_drives/', views.my_applied_drives, name='my_applied_drives'),

   path('apply-activity/<int:activity_id>/', views.apply_activity, name='apply_activity'),
    path('activity/application/exists/', views.activity_application_exists, name='activity_application_exists'),
    path('activity/applied_students/<int:activity_id>/', views.applied_students_for_activity, name='activity_applied_students'),


    

]
