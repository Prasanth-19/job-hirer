from django.db import models
from django.utils import timezone

# Create your models here.
class UserMaster(models.Model):
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    otp=models.IntegerField()
    role=models.CharField(max_length=10)
    is_active=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now_add=True)
    
class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, default='')
    lastname = models.CharField(max_length=50, default='')
    contact = models.CharField(max_length=25, default='')
    city = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=150, default='')
    dob = models.DateField(null=True,blank=True)  # Use DateField for better date handling
    gender = models.CharField(max_length=10, default='')
    min_salary = models.BigIntegerField(default=0)
    max_salary = models.BigIntegerField(default=0)
    job_type = models.CharField(max_length=50, default='')
    job_category = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    highest_education = models.CharField(max_length=50, default='')
    experience = models.CharField(max_length=50, default='')  # Corrected typo
    website = models.CharField(max_length=150, default='')
    shifts = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=550, default='')
    pincode = models.CharField(max_length=10, default='') 
    area = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    profile_pic = models.ImageField(upload_to="app/img/candidate")  
    
     
class Company(models.Model):
    user_id=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    company_name=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    website=models.CharField(max_length=150,default='')
    description=models.TextField(max_length=200,default='')
    logo_pic=models.ImageField(upload_to="app/img/company")
    
    
    '''job details '''
class JobDetails(models.Model):
    company_id =models.ForeignKey(Company,on_delete=models.CASCADE,default="")
    job_name =models.CharField(max_length=100)
    company_name =models.CharField(max_length=100)
    company_address =models.CharField(max_length=200)
    job_description =models.CharField(max_length=200)
    qualification =models.CharField(max_length=100)
    responsibilities =models.TextField(default="no specific responsibility is required ")
    location =models.CharField(max_length=150)
    company_website =models.CharField(max_length=150)
    company_email =models.CharField(max_length=50)
    company_contact =models.CharField(max_length=50)
    salary =models.CharField(max_length=50)
    experience =models.CharField(max_length=50,default=None)
    logo =models.ImageField(upload_to="app/img/jobpost",default="")
    created_at=models.DateField(default=timezone.now)
    shifts=models.CharField(max_length=20,default="full time ")
    dead_line=models.DateField(default=timezone.now)
    
class ApplyJob(models.Model):
    candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job=models.ForeignKey(JobDetails,on_delete=models.CASCADE)
    education=models.CharField(max_length=100)
    website=models.CharField(max_length=200)
    gender=models.CharField(max_length=10)
    resume=models.FileField(upload_to="app/resumes")
    experience=models.CharField(max_length=50)
    coverletter=models.TextField()
    email=models.CharField(max_length=30)
    contact=models.IntegerField()
    submitted_at = models.DateTimeField(default=timezone.now)
    
    
    
class Queries(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=200)
    submitted_at = models.DateTimeField(default=timezone.now)