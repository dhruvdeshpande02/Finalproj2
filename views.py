from .models import Student,Coordinator,TNPOffice,Drive, DriveApplication,Activity,ActivityApplication
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from .forms import StudentForm,CustomUserForm,CoordinatorForm,TNPOfficeForm,LoginForm
from django.contrib.auth.decorators import login_required

def register_student(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST,view_name='register_student')
        student_form = StudentForm(request.POST, request.FILES)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()

            user.set_password(user_form.cleaned_data["password1"])
            user.save()
            Student.objects.create(user=user, **student_form.cleaned_data)
            print("DATA:",student_form.cleaned_data )
            user.backend = 'users.authentication.EmailBackend'             
            login(request, user)
            return redirect('dashboard')
                
        else:
            # Print form errors for debugging
            print("User Form Data:", user_form.cleaned_data)  # Print user form data
    else:
        user_form = CustomUserForm(view_name='register_student')
        student_form = StudentForm()

    return render(request, 'student_registration.html', {'user_form': user_form, 'student_form': student_form, })



def register_coordinator(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        coordinator_form = CoordinatorForm(request.POST, request.FILES)
        if user_form.is_valid() and coordinator_form.is_valid():
            user = user_form.save()

            user.set_password(user_form.cleaned_data["password1"])
            user.save()
            Coordinator.objects.create(user=user, **coordinator_form.cleaned_data)
            # print("DATA:",student_form.cleaned_data )
            user.backend = 'users.authentication.EmailBackend'             
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful registration
    else:
        user_form = CustomUserForm()
        coordinator_form = CoordinatorForm()
        
    return render(request, 'coordinator_registration.html', {'user_form': user_form, 'coordinator_form': coordinator_form, })

def register_tnpoffice(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        tnpoffice_form = TNPOfficeForm(request.POST, request.FILES)
        if user_form.is_valid() and tnpoffice_form.is_valid():
            user = user_form.save()

            user.set_password(user_form.cleaned_data["password1"])
            user.save()
            TNPOffice.objects.create(user=user, **tnpoffice_form.cleaned_data)
            # print("DATA:",student_form.cleaned_data )
            user.backend = 'users.authentication.EmailBackend'             
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful registration
    else:
        user_form = CustomUserForm()
        tnpoffice_form = TNPOfficeForm()
        
    return render(request, 'tnpoffice_registration.html', {'user_form': user_form, 'tnpoffice_form': tnpoffice_form, })



def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      user = authenticate(request, email=email, password=password)
      if user is not None:
        login(request, user)
        return redirect('dashboard')  # Replace 'dashboard' with your desired redirect URL
      else:
        # Handle invalid credentials error message
        pass
  else:
    form = LoginForm()
  return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        # If the request method is POST, it means the user has confirmed logout
        logout(request)
        # Redirect the user to the login page or any other page you prefer
        return redirect('login')
    else:
        # If the request method is not POST, render the logout confirmation page
        return render(request, 'logout.html')


@login_required
def all_students(request):
    students = Student.objects.all()
    return render(request, 'all_students.html',{'students': students})
@login_required
def all_coordinators(request):
    coordinators = Coordinator.objects.all()
    return render(request, 'all_coordinators.html',{'coordinators': coordinators})


from django.contrib.auth.decorators import login_required
@login_required
def apply_drive(request, drive_id):
    drive = get_object_or_404(Drive, drive_id=drive_id)
    student = request.user.student

    # Check if the student has already applied to this drive
    application = DriveApplication.objects.filter(student=student, drive=drive).first()
    if not application:
        # If the application doesn't exist, create a new DriveApplication object
        application = DriveApplication.objects.create(student=student, drive=drive)
        return redirect('application_success')
    else:
        # If the application exists, redirect to 'application_exists'
        return redirect('drive_application_exists')
@login_required
def application_success(request):
    return render(request, 'application_success.html')
@login_required
def drive_application_exists(request):
    
    return render(request, 'drive_application_exists.html')


@login_required
def applied_students_for_drive(request, drive_id):
    drive = get_object_or_404(Drive, pk=drive_id)
    drive_applications = DriveApplication.objects.filter(drive=drive)
    applied_students = [application.student for application in drive_applications]
    return render(request, 'applied_students_for_drive.html', {'drive': drive, 'applied_students': applied_students,'drive_applications':drive_applications})

@login_required
def my_applied_drives(request):
    # Get the current logged-in student
    student = request.user.student
    # Filter DriveApplication objects for the current student
    applied_drives = DriveApplication.objects.filter(student=student)
    applied_activities =ActivityApplication.objects.filter(student=student)
    context = {'applied_drives': applied_drives,'applied_activities': applied_activities}
    return render(request, 'my_applications.html',context)

@login_required
def apply_activity(request, activity_id):
    activity = get_object_or_404(Activity, activity_id=activity_id)
    student = request.user.student

    # Check if the student has already applied to this drive
    application = ActivityApplication.objects.filter(student=student, activity=activity).first()
    if not application:
        # If the application doesn't exist, create a new DriveApplication object
        application = ActivityApplication.objects.create(student=student, activity=activity)
        return redirect('application_success')
    else:
        # If the application exists, redirect to 'application_exists'
        return redirect('activity_application_exists')

@login_required
def activity_application_exists(request):
    
    return render(request, 'activity_application_exists.html')    

@login_required
def applied_students_for_activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    activity_applications = ActivityApplication.objects.filter(activity=activity)
    applied_students = [application.student for application in activity_applications]
    return render(request, 'applied_students_for_activity.html', {'activity': activity, 'applied_students': applied_students,'activity_applications':activity_applications})
