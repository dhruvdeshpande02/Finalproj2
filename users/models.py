from django.db import models
from notices.models import Department
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_CHOICES = [
        ('S', 'Student'),
        ('C', 'Coordinator'),
        ('T-O', 'TNP-Office'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_CHOICES,default ='Student')

    # Specify email as the USERNAME_FIELD
    USERNAME_FIELD = 'email'
    
    # Remove email from REQUIRED_FIELDS
    REQUIRED_FIELDS = []

    # Ensure email is marked as unique
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,blank=True)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    YEAR_CHOICES = [
        ('3rd year', '3rd year'),
        ('Btech', 'Btech'),
    ]

    FIRST_NAME = models.CharField(max_length=255)
    MIDDLE_NAME = models.CharField(max_length=255)
    LAST_NAME= models.CharField(max_length=255)
    PRN = models.PositiveIntegerField(unique=True)
    DOB = models.DateField()
    GENDER = models.CharField(max_length=10, choices=GENDER_CHOICES)
    EMAIL = models.EmailField(unique=True)
    PERSONAL_EMAIL = models.EmailField(unique=True)
    AGE = models.PositiveIntegerField()
    MOBILE_NO = models.PositiveIntegerField()
    ALT_Mobile_NO = models.PositiveIntegerField()
    LOCAL_ADDRS = models.CharField(max_length=255)
    PERM_ADDRS = models.CharField(max_length=255)
    Native_Place = models.CharField(max_length=255)
    X_Percentage = models.DecimalField(max_digits=5, decimal_places=2)
    Xth_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)
    X_year_of_passing = models.PositiveIntegerField()
    X_board = models.CharField(max_length=255)
    XIIth_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)
    XII_Percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    XII_year_of_passing = models.PositiveIntegerField(null=True, blank=True)
    XII_board = models.CharField(max_length=255, null=True, blank=True)
    Diploma_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Diploma_Firstyear_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)    
    Diploma_Secondyear_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)    
    Diploma_Thirdyear_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)    
    Diploma_year_of_passing = models.PositiveIntegerField(null=True, blank=True)
    Diploma_college = models.CharField(max_length=255, null=True, blank=True)
    Diploma_branch = models.CharField(max_length=255, null=True, blank=True)
    Admission_Type = models.CharField(max_length=255)
    YEAR = models.CharField(max_length=10, choices=YEAR_CHOICES )
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    Engg_year_of_passing = models.PositiveIntegerField()
    SEM_1_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    sem1_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)
    SEM_2_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    sem2_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)
    SEM_3_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    sem3_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)
    SEM_4_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    sem4_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)
    SEM_5_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    sem5_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)
    SEM_6_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    sem6_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)
    SEM_7_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem7_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)
    SEM_8_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem8_marksheet = models.FileField(upload_to='images/documents/', null=True, blank=True)
    AVG_TILL_SEM_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    AVG_TILL_SEM_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Live_backlogs = models.PositiveIntegerField()
    Dead_backlogs = models.CharField(max_length=255)
    Year_gap = models.CharField(max_length=255)
    Preference_1 = models.CharField(max_length=255)
    Preference_2 = models.CharField(max_length=255)
    Preference_3 = models.CharField(max_length=255)
    Placed = models.CharField(max_length=255)
    Profile_photo = models.ImageField(upload_to='images/profiles/')
    

    def calculate_average_and_percentage(self):
        sem_sgpa_fields = [self.SEM_1_sgpa, self.SEM_2_sgpa, self.SEM_3_sgpa, self.SEM_4_sgpa, self.SEM_5_sgpa, self.SEM_6_sgpa, self.SEM_7_sgpa, self.SEM_8_sgpa]
        valid_sgpa_values = [sgpa for sgpa in sem_sgpa_fields if sgpa is not None]
        
        if valid_sgpa_values:
            avg_cgpa = sum(valid_sgpa_values) / len(valid_sgpa_values)
            self.AVG_TILL_SEM_cgpa = round(avg_cgpa, 2)
            
            max_sgpa = 10  # Assuming 10 is the maximum SGPA
            percentage = (avg_cgpa / max_sgpa) * 100
            self.AVG_TILL_SEM_percentage = round(percentage, 2)

    def clean(self):
        # Check if either XIIth fields or Diploma fields are filled, but not both
        if (
            (self.XII_Percentage is not None or self.XII_year_of_passing is not None or self.XII_board) and
            (self.Diploma_percentage is not None or self.Diploma_year_of_passing is not None or self.Diploma_college or self.Diploma_branch)
        ):
            raise ValidationError("Either fill the XIIth fields or the Diploma fields, but not both.")
    def save(self, *args, **kwargs):
        self.calculate_average_and_percentage()
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.FIRST_NAME
       
    

from django.db import models

class Coordinator(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    NAME = models.CharField(max_length=255)
    PHONE_NO = models.PositiveIntegerField()
    EMAIL = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    PERSONAL_EMAIL = models.EmailField()
    C_ID =  models.PositiveIntegerField(unique=True)
    INSTITUTE = models.CharField(max_length=255)
    PROFILE_PHOTO = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.NAME