from django.urls import path
from . import views

urlpatterns = [
    
    path('all-drives/',views.drives, name ='all-drives'),
    path('drive/<str:pk>/',views.drive, name='drive'),
    path('create-drive/',views.createDrive,name='create-drive'),
    path('update-drive/<str:pk>/',views.updateDrive, name='update-drive'),
    path('delete-drive/<str:pk>/', views.delete_Drive, name='delete-drive'),
    path('activities/', views.activities, name='activities'),
    path('activity/<str:pk>/',views.activity, name='activity'),
    path('create-activity/',views.createActivity,name='create-activity'),
    path('update-activity/<str:pk>/',views.updateActivity, name='update-activity'),
    path('delete-activity/<str:pk>/', views.delete_Activity, name='delete-activity'),
    path('view/',views.my_view, name='view'),
    path('sidebar/',views.sidebar, name='sidebar'),

    path('dashboard/',views.dashboard, name='dashboard'),





    ]