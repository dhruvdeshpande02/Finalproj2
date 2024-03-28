


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import authenticate  # Import the authenticate function
from django import forms
from .models import CustomUser, Student,Coordinator,TNPOffice
class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'user_type']  # Include required fields directly

    def __init__(self, *args, view_name=None, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email Address'  # Customize email label

        if view_name == 'register_student':
            self.fields['user_type'].widget = forms.HiddenInput()
                    # ... other field customizations for user_type if needed ...
    def clean_user_type(self):
        user_type = self.cleaned_data.get('user_type')
        # Perform any additional validation if needed
        return user_type            
                  

class StudentForm(forms.ModelForm):
  class Meta:
        model = Student
        fields = '__all__'  # Include all fields by default
        exclude = ['user','AVG_TILL_SEM_cgpa','AVG_TILL_SEM_percentage']  

class CoordinatorForm(forms.ModelForm):
   class Meta:
         model =Coordinator
         fields = '__all__'
         exclude = ['user']

class TNPOfficeForm(forms.ModelForm):
  class Meta:
        model = TNPOffice
        fields = '__all__'  # Include all fields by default
        exclude = ['user']  

from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
  email = forms.EmailField(max_length=254)
  password = forms.CharField(widget=forms.PasswordInput)

  def clean(self):
    cleaned_data = super().clean()
    email = cleaned_data.get('email')
    password = cleaned_data.get('password')
    user = authenticate(email=email, password=password)
    if not user:
      raise forms.ValidationError('Invalid email or password')
    return cleaned_data
  

