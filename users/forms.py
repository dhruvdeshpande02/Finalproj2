


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import authenticate  # Import the authenticate function
from django import forms
from .models import CustomUser, Student
class CustomUserForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ['email']
              

class StudentForm(forms.ModelForm):
  class Meta:
        model = Student
        fields = '__all__'  # Include all fields by default
        exclude = ['user','AVG_TILL_SEM_cgpa','AVG_TILL_SEM_percentage']  



