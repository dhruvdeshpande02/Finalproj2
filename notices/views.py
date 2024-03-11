from django.shortcuts import render,redirect,get_object_or_404
from .models import Drive,Activity,Department

from .forms import DriveForm,ActivityForm
# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def sidebar (request):
    return render(request,'sidebar.html')

def my_view(request):
    departments = Department.objects.all()
    print(departments)  # This will print the queryset in your console or terminal
    # Other code in your view
    return render(request, 'my_template.html', {'departments': departments})

def drives(request):
    alldrives = Drive.objects.all()
    return render(request, 'all-drives.html', {'alldrives': alldrives})
    
def drive(request, pk):
    drive = Drive.objects.get(drive_id=pk)
    return render(request, 'single-drive.html', {'drive': drive})    



def createDrive(request):
    if request.method == 'POST':
        form = DriveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all-drives')  # Redirect to a success page or any other URL
    else:
        form = DriveForm()
    return render(request, 'create_drive.html', {'form': form})

# views.py



def updateDrive(request, pk):
    drive = get_object_or_404(Drive, drive_id=pk)
    form = DriveForm(instance=drive)
    if request.method == 'POST':
        form = DriveForm(request.POST, request.FILES, instance=drive)
        if form.is_valid():
            form.save()
            return redirect('all-drives')  # Redirect to any appropriate URL
    context = {'form': form}
    return render(request, 'create_drive.html', context)

def delete_Drive(request, pk):
    drive = get_object_or_404(Drive, drive_id=pk)
    if request.method == 'POST':
        drive.delete()
        return redirect('all-drives')
    context ={'drive': drive}
    return render(request, 'delete_drive.html', context)


#--------------------------------------- ACTIVITY VIEWS------------------------------------------
def activities(request):
    activities = Activity.objects.all()
    context ={'activities':activities}
    return render(request, 'activities.html', context)

def activity(request, pk):
    activity = Activity.objects.get(activity_id=pk)
    context={'activity':activity}
    return render(request, 'activity.html',context)  

def createActivity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('activities')  # Redirect to a success page or any other URL
    else:
        form = ActivityForm()
        context={'form':form}
    return render(request, 'create_activity.html', context)

def updateActivity(request, pk):
    activity = get_object_or_404(Activity, activity_id=pk)
    form = ActivityForm(instance=activity)
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activities')  # Redirect to any appropriate URL
    context = {'form': form}
    return render(request, 'create_activity.html', context)


def delete_Activity(request, pk):
    activity = get_object_or_404(Activity, activity_id=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('activities')  # Redirect to any appropriate URL
    context={'activity':activity}
    return render(request, 'delete_activity.html', context)