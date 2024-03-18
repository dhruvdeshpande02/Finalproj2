


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import authenticate  # Import the authenticate function
from django import forms
from .models import CustomUser, Student,Coordinator
class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'user_type']  # Include required fields directly

    def __init__(self, *args, view_name=None, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email Address'  # Customize email label

        if view_name in ['register_student']:
            self.fields['user_type'].widget.attrs.update({'disabled': True})
                    # ... other field customizations for user_type if needed ...
                
                  

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
