from django.db import models
# Create your models here.
from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)


    def __str__(self):
        return self.name

class Drive(models.Model):

     
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=30)
    company_logo = models.ImageField(null=True,blank=True)
    date = models.DateField()
    content = models.TextField()
    Bond = models.CharField(max_length=50)
    industry_type = models.CharField(max_length=50) 
    department = models.ManyToManyField(Department)
    job_role = models.CharField(max_length=50)
    job_location = models.CharField(max_length=50)
    job_eligibility = models.TextField()
    selection_process = models.TextField()
    job_CTC = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    drive_id = models.AutoField(primary_key=True)


    def __str__(self):
        return self.title
    class Meta:
        ordering = ['creation_date']


from django.db import models

class Activity(models.Model):        
    activity_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    company_logo = models.ImageField(null=True,blank=True)
    company_name = models.CharField(max_length=255)
    industry_type = models.CharField(max_length=255)
    activity_date = models.DateField()
    department = models.ManyToManyField(Department)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['creation_date']