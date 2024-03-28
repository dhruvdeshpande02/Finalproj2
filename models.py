from django.db import models
from notices.models import Department,Drive,Activity
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_CHOICES = [
        ('Student', 'Student'),
        ('Coordinator', 'Coordinator'),
        ('TNP-Office', 'TNP-Office'),
    ]
    user_type = models.CharField(max_length=15, choices=USER_CHOICES,default ='Student')
    username = models.CharField(max_length=10,null=True,blank=True)
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

    Gap =[
        ('0','0'),
        ('1','1'),
        ('1','1'),

    ]
    Boolean_choices =[
        ('N','No'),
        ('Y','Yes'),
    ]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]


    FIRST_NAME = models.CharField(max_length=255)
    MIDDLE_NAME = models.CharField(max_length=255)
    LAST_NAME= models.CharField(max_length=255)
    PRN = models.PositiveIntegerField(unique=True)
    DOB = models.DateField(null=True, blank=True)
    GENDER = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    EMAIL = models.EmailField(unique=True, null=True, blank=True)
    PERSONAL_EMAIL = models.EmailField(unique=True, null=True, blank=True)
    AGE = models.PositiveIntegerField(null=True, blank=True)
    MOBILE_NO = models.PositiveIntegerField(null=True, blank=True)
    ALT_Mobile_NO = models.PositiveIntegerField(null=True, blank=True)
    LOCAL_ADDRS = models.CharField(max_length=255, null=True, blank=True)
    PERM_ADDRS = models.CharField(max_length=255, null=True, blank=True)
    Native_Place = models.CharField(max_length=255, null=True, blank=True)
    X_Percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Xth_marksheet = models.FileField(upload_to='documents/10th', null=True, blank=True)
    X_year_of_passing = models.PositiveIntegerField(null=True, blank=True)
    X_board = models.CharField(max_length=255, null=True, blank=True)
    XIIth_marksheet = models.FileField(upload_to='documents/12th', null=True, blank=True)
    XII_Percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    XII_year_of_passing = models.PositiveIntegerField(null=True, blank=True)
    XII_board = models.CharField(max_length=255, null=True, blank=True)
    Diploma_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Diploma_Firstyear_marksheet = models.FileField(upload_to='documents/diploma1', null=True, blank=True)    
    Diploma_Secondyear_marksheet = models.FileField(upload_to='documents/diploma2', null=True, blank=True)    
    Diploma_Thirdyear_marksheet = models.FileField(upload_to='documents/diploma3', null=True, blank=True)    
    Diploma_year_of_passing = models.PositiveIntegerField(null=True, blank=True)
    Diploma_college = models.CharField(max_length=255, null=True, blank=True)
    Diploma_branch = models.CharField(max_length=255, null=True, blank=True)
    Admission_Type = models.CharField(max_length=255, null=True, blank=True)
    YEAR_CHOICES = [(str(year), str(year)) for year in range(2020, 2031)]
    Pass_out_Year = models.CharField(max_length=10, choices=YEAR_CHOICES, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)   
    SEM_1_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem1_marksheet = models.FileField(upload_to='documents/Sem1', null=True, blank=True)
    SEM_2_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem2_marksheet = models.FileField(upload_to='documents/Sem2', null=True, blank=True)
    SEM_3_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem3_marksheet = models.FileField(upload_to='images/documents/Sem3', null=True, blank=True)
    SEM_4_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem4_marksheet = models.FileField(upload_to='documents/Sem4', null=True, blank=True)
    SEM_5_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem5_marksheet = models.FileField(upload_to='documents/Sem5', null=True, blank=True)
    SEM_6_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem6_marksheet = models.FileField(upload_to='documents/Sem6', null=True, blank=True)
    SEM_7_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem7_marksheet = models.FileField(upload_to='documents/Sem7', null=True, blank=True)
    SEM_8_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem8_marksheet = models.FileField(upload_to='documents/Sem8', null=True, blank=True)
    AVG_TILL_SEM_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    AVG_TILL_SEM_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Live_backlogs = models.PositiveIntegerField(null=True, blank=True,choices=Boolean_choices)
    Dead_backlogs = models.CharField(max_length=255, null=True, blank=True,choices=Boolean_choices,)
    Year_gap = models.CharField(max_length=255, null=True, blank=True,choices=Gap)
    Preference_1 = models.CharField(max_length=255, null=True, blank=True)
    Preference_2 = models.CharField(max_length=255, null=True, blank=True)
    Preference_3 = models.CharField(max_length=255, null=True, blank=True)
    Placed = models.CharField(max_length=255, null=True, blank=True)
    Profile_photo = models.ImageField(upload_to='images/profiles/student', null=True, blank=True)

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
        return f"{self.FIRST_NAME} - {self.PRN}"
       
    

from django.db import models

class Coordinator(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    C_ID =  models.CharField(max_length = 25,unique=True)
    NAME = models.CharField(max_length=255)
    GENDER = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    PHONE_NO = models.PositiveIntegerField()
    EMAIL = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    PERSONAL_EMAIL = models.EmailField()
    INSTITUTE = models.CharField(max_length=255)
    PROFILE_PHOTO = models.ImageField(upload_to='images/profiles/Coordinator',null=True,blank=True)

    def __str__(self):
        return self.NAME
    


from django.db import models

class TNPOffice(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    T_ID =  models.CharField(max_length = 25,unique=True)
    NAME = models.CharField(max_length=255)
    PHONE_NO = models.PositiveIntegerField()
    EMAIL = models.EmailField()
    PERSONAL_EMAIL = models.EmailField()
    PROFILE_PHOTO = models.ImageField(upload_to='images/profiles/tnp',null=True,blank=True)

    def __str__(self):
        return self.NAME
    

class DriveApplication(models.Model):
    drive= models.ForeignKey(Drive, on_delete=models.CASCADE)  # Notice the student applied for
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Student applying for the notice
    applied_date = models.DateTimeField(auto_now_add=True)  # Date/time the application was submitted
      # Optional link to the student's resume

    class Meta:
        unique_together = (('drive', 'student'),)  # Ensure a student can only apply for a notice once

    def __str__(self):
        return f"{self.student.FIRST_NAME} - {self.drive.title}"        
    
class ActivityApplication(models.Model):
    activity= models.ForeignKey(Activity, on_delete=models.CASCADE)  # Notice the student applied for
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Student applying for the notice
    applied_date = models.DateTimeField(auto_now_add=True)  # Date/time the application was submitted

    class Meta:
        unique_together = (('activity', 'student'),)  # Ensure a student can only apply for a notice once

    def __str__(self):
        return f"{self.student.FIRST_NAME} - {self.activity.title}"            