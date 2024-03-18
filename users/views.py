from .models import Student,Coordinator
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from .forms import StudentForm,CustomUserForm,CoordinatorForm

def all_students(request):
    students = Student.objects.all()
    return render(request, 'all_students.html',{'students': students})

def register_student(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        student_form = StudentForm(request.POST, request.FILES)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()

            user.set_password(user_form.cleaned_data["password1"])
            user.save()
            Student.objects.create(user=user, **student_form.cleaned_data)
            print("DATA:",student_form.cleaned_data )
            user.backend = 'users.authentication.EmailBackend'             
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful registration
    else:
        user_form = CustomUserForm()
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

from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      # User is authenticated, redirect to desired page
      return redirect('dashboard')  # Replace 'home' with your desired redirect URL
  else:
    form = LoginForm()
  return render(request, 'login.html', {'form': form})

def logout_view(request):
  # Logout the user (works for both regular users and admins)
  logout(request)

  # Redirect to a specific logout page (optional)
  return render(request, 'logout.html')






        # def user_login(request):
        #     if request.method == 'POST':
        #         form = CustomAuthenticationForm(request, data=request.POST)
        #         if form.is_valid():
        #             user = form.get_user()
        #             login(request, user)  # Log in the user
        #             return redirect('home')  # Redirect to the home page after successful login
        #     else:
        #         form = CustomAuthenticationForm()
        #     return render(request, 'login.html', {'form': form})
