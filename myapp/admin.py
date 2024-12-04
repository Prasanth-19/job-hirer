from django.contrib import admin

# Register your models here.
from .models import *  # Import your model here

admin.site.register(UserMaster)
admin.site.register(Candidate)
admin.site.register(Company)
admin.site.register(JobDetails)
admin.site.register(ApplyJob)
admin.site.register(Queries)
#admin panel details (username:prasanth,email:minemine@gmail.com,password:kingler)