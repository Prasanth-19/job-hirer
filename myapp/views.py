from django.shortcuts import render,redirect,get_object_or_404
from random import randint
from django.http import HttpResponse 
from .models import UserMaster,ApplyJob,Candidate,Company,JobDetails,Queries


# Create your views here.


def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})


def IndexPage(request):
    jobs=JobDetails.objects.all().order_by("-id")[:5]
    return render(request,"index.html",{"jobs":jobs})

def cus(request):
    return render(request,"cus.html")

def Contactquery(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject=request.POST.get('subject')
            message = request.POST.get('message')
            
            print(name,email,subject,message)
            new_query=Queries.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            new_query.save()
            print(name,email,subject,message)
            message="data sent successfully"
            return render(request,"index_message.html",{'msg': message})
        else:
            return render(request, "cus.html")
    except Exception as e:
        print("Error:", e)
        return render(request, "error.html", {'error': str(e)})

def otps(request):
    o=UserMaster.objects.all().order_by("-id")
    return render(request,"otps.html",{"o":o})

def CandidatePage(request):
    jobs=JobDetails.objects.all().order_by("-id")[:5]
    return render(request,"candidatepage.html",{"jobs":jobs})

def SignupPage(request):
    return render(request,"registration.html")

def logout_page(request):
    try:
        if 'email' in request.session and 'password' in request.session :
            user = UserMaster.objects.get(email=request.session['email'])
            user.is_active = False
            user.save()
            del request.session['email']
            del request.session['password']
            return redirect('index')
        request.session.flush()
        return redirect('index')
    #except:
     #   return redirect('index')
    except Exception as e:
        print("Error:", e)
        return render(request, "error.html", {'error': str(e)})
    
def Aboutus(request):
    return render(request,"about.html")

def Contact(request):
    return render(request,"contact.html")

def Contact_query(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject=request.POST.get('subject')
            message = request.POST.get('message')
            
            print(name,email,subject,message)
            new_query=Queries.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            new_query.save()
            print(name,email,subject,message)
            message="data sent successfully"
            return render(request,"message.html",{'msg': message})
        else:
            return render(request, "contact.html")
    except Exception as e:
        print("Error:", e)
        return render(request, "error.html", {'error': str(e)})


def RegisterUser(request):
    if request.method == "POST":
        role = request.POST.get('role')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('Email')  # Use consistent variable naming
        password = request.POST.get('Password')
        cpassword = request.POST.get('Cpassword')

        if role == 'Candidate':
            user = UserMaster.objects.filter(email=email).first()
            if user:
                message = "User already exists"
                return render(request, "registration.html", {'msg': message})
            else:
                if password == cpassword:
                    otp = randint(100000, 999999)
                    newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                    new_candidate = Candidate.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                    return redirect('otpVerification', email=email)
                else:
                    message = "Passwords do not match"
                    return render(request, "registration.html", {'msg': message})
        elif role == 'Company':
            user = UserMaster.objects.filter(email=email).first()
            if user:
                message = "User already exists"
                return render(request, "registration.html", {'msg': message})
            else:
                if password == cpassword:
                    otp = randint(100000, 999999)
                    newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                    new_company = Company.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                    return redirect("otpVerification", email=email)
                else:
                    message = "Passwords do not match"
                    return render(request, "registration.html", {'msg': message})
        else:
            message = "Invalid role"
            return render(request, "registration.html", {'msg': message})
    else:
        return render(request, "registration.html")


def OtpVerification(request,email):
    print("Rendering OTP verification page for email:", email)
    return render(request, "otp.html", {'email': email})

def OtpVerify(request):
    if request.method == "POST":
        email = request.POST.get('email')
        otp = int(request.POST.get('otp', 0))

        print(f"Submitted Email: {email}")
        print(f"Submitted OTP: {otp}")

        try:
            user = UserMaster.objects.get(email=email)
            if user:
                if user.otp == otp:
                    message = "OTP verified successfully"
                    user.is_verified=True
                    user.save()
                    return render(request, "login.html", {'msg': message})
                else:
                    message = "OTP is incorrect"
                    print("OTP is incorrect, returning email:", email)
                    return render(request, "otp.html", {'msg': message, 'email': email})
        except UserMaster.DoesNotExist:
            return render(request, "registration.html")
    return render(request, "registration.html")


def  loginPage(request):
    return render(request,"login.html")

def TermsAndConditions(request):
    return render(request,"termsandconditions.html")

def ResendOtp(request,email):
    try:
        user=UserMaster.objects.get(email=email)
        new_otp=randint(100000, 999999)
        user.save()
        message="otp sent successfully"
        return render(request,"otp.html",{'email':email,'msg':message})
    except UserMaster.DoesNotExist:
        message="user not existed"
        return render(request,"registration.html",{'msg':message})


def ForgotPassword(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user=UserMaster.objects.get(email=email)
            new_otp=randint(100000, 999999)
            user.otp=new_otp
            user.save()
            message="otp sent successfully"
            return render(request,"verify_otp.html",{'msg':message,'email':email})
        
        except UserMaster.DoesNotExist:
            message="user not existed"
            return render(request,"forgot_password.html",{'msg':message})
    return render(request,"forgot_password.html")







def VerifyOtp(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        new_password = request.POST.get('password')
        c_password = request.POST.get('cpassword')

        try:
            user = UserMaster.objects.get(email=email)

            if user.otp == int(otp):
                if new_password == c_password:
                    user.password=new_password
                    user.save()
                    message = "Password changed successfully"
                    return render(request, "login.html", {'msg': message})
                else:
                    message = "Password and confirm password do not match"
                    return render(request, "verify_otp.html", {'msg': message, 'email': email})
            else:
                message = "OTP does not match"
                return render(request, "verify_otp.html", {'msg': message, 'email': email})
        except UserMaster.DoesNotExist:
            message = "User does not exist"
            return render(request, "forgot_password.html", {'msg': message})

    return render(request, "verify_otp.html")


def LoginUser(request):
    if request.method == "POST":
       

        role = request.POST.get('role')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = UserMaster.objects.get(email=email)
            
            if user.password != password:
                message = "Password is wrong"
                return render(request, "login.html", {'msg': message})
            
            if role == "Candidate":
                try:
                    
                    candidate = Candidate.objects.get(user_id=user)
                    request.session["user_id"] = user.id
                    request.session["role"] = user.role
                    request.session["firstname"] = candidate.firstname
                    request.session["lastname"] = candidate.lastname
                    request.session["email"] = user.email
                    request.session["password"] = user.password
                    user.is_active=True
                    user.save()
                    return redirect('cpage')
                except Candidate.DoesNotExist:
                    message = "Candidate profile does not exist"
                    return render(request, "login.html", {'msg': message})
            
            elif role == "Company":
                try:
                    
                    company = Company.objects.get(user_id=user) 
                    request.session["user_id"] = user.id
                    request.session["role"] = user.role
                    request.session["firstname"] = company.firstname  
                    request.session["lastname"] = company.lastname
                    request.session["email"] = user.email
                    user.is_active=True
                    user.save()
                    return redirect('compage')
                except Company.DoesNotExist:
                    message = "Company profile does not exist"
                    return render(request, "login.html", {'msg': message})
            
            else:
                message = "Select the role"
                return render(request, "login.html", {'msg': message})
        
        except UserMaster.DoesNotExist:
            message = "User does not exist"
            return render(request, "login.html", {'msg': message})
    
    return render(request, "login.html")


def ProfilePage(request,pk):
    user=UserMaster.objects.get(pk=pk)
    can=Candidate.objects.get(user_id=user)
    return render(request,"profile.html",{'can':can,'user':user})

def UpdateProfile(request, pk):
    try:
        if request.method == "POST":
            print("POST Data:", request.POST)
            user = UserMaster.objects.get(pk=pk)
            if user.role == "Candidate":
                can = Candidate.objects.get(user_id=user)
                can.contact = request.POST.get('con', '')
                can.city = request.POST.get('_city', 'unknown')
                can.address = request.POST.get('_address', 'unknown')
                can.dob = request.POST.get('d_o_b', '2000-01-01')  # Default value
                can.gender = request.POST.get('gender', 'unknown')
                can.min_salary = request.POST.get('min_s', 0) or 0
                can.state = request.POST.get('stat_e', 'unknown')
                can.max_salary = request.POST.get('max_s', 0) or 0
                can.job_type = request.POST.get('j_type', 'unknown')
                can.job_category = request.POST.get('j_cat', 'unknown')
                can.country = request.POST.get('coun', 'unknown')
                can.highest_education = request.POST.get('edu', 'unknown')
                can.experience = request.POST.get('exp', 'unknown')
                can.website = request.POST.get('web', 'unknown')
                can.shifts = request.POST.get('shift', 'unknown')
                can.description = request.POST.get('desc', 'unknown')
                can.pincode = request.POST.get('postal', '000000')  # Default value for empty pincode
                can.area = request.POST.get('area', 'unknown')

                if 'profile_pic' in request.FILES:
                    can.profile_pic = request.FILES['profile_pic']
                    print("Profile pic uploaded:", request.FILES['profile_pic'])
                else:
                    print("No profile pic in request.FILES")

                can.save()
                print("Profile saved:", can.profile_pic.url if can.profile_pic else "No profile pic")
                url = f'/profilepage/{pk}'
                return redirect(url)
            else:
                return render(request, "candidatepage.html", {'pk': pk})
    except UserMaster.DoesNotExist:
        print("UserMaster.DoesNotExist")
        return render(request, "404.html")
    except Candidate.DoesNotExist:
        print("Candidate.DoesNotExist")
        return render(request, "404.html")
    except Exception as e:
        print("Error:", e)
        return render(request, "error.html", {'error': str(e)})

def Job_List(request):
    all_jobs=JobDetails.objects.all()
    return render(request,'job-list.html',{'alljobs':all_jobs})



def Job_Details(request, pk):
    job_details = get_object_or_404(JobDetails, pk=pk)
    com = job_details.company_id 
    return render(request, "job-detail.html", {"jdetails": job_details, "comp": com})


    
def Job_ApplyPage(request, pk):
    try:
        user_id = request.session.get('user_id')
        if user_id:
            cand = Candidate.objects.get(user_id=user_id)
            job = JobDetails.objects.get(id=pk)
                
            return render(request, "job-form.html", {"user": user_id, "cand": cand, "job": job})
        else:
            message = "User doesn't exist"
            return render(request, "message.html", {'msg': message})
    except Exception as e:
        print("Error:", e)
        return render(request, "error.html", {'error': str(e)})
    
    

def Apply_Job(request, pk):
    try:
        if request.method == "POST":
            user_id = request.session.get('user_id')
            print(f"User ID from session: {user_id}")
            
            if user_id:
                can = Candidate.objects.get(user_id=user_id)
                print(f"Candidate: {can}")
                job = JobDetails.objects.get(id=pk)
                print(f"Job: {job}")
                
                # Retrieve form data
                edu = request.POST.get('education')
                web = request.POST.get('website')
                gender = request.POST.get('gender')
                email = request.POST.get('email')
                contact = request.POST.get('contact')
                c_letter = request.POST.get('cover_letter')
                resume = request.FILES.get('resume')
                
                # Debug print statements to check values
                print(f"Education: {edu}")
                print(f"Website: {web}")
                print(f"Gender: {gender}")
                print(f"Email: {email}")
                print(f"Contact: {contact}")
                print(f"Cover Letter: {c_letter}")
                print(f"Resume: {resume}")
                
                # Save the application
                new_apply = ApplyJob.objects.create(
                    candidate=can,
                    job=job,
                    education=edu,
                    website=web,
                    gender=gender,
                    email=email,
                    contact=contact,
                    coverletter=c_letter,
                    resume=resume
                )
                
                message = "Job applied successfully"
                print("Job application saved successfully")
                return render(request, "message.html", {'msg': message})
            else:
                message = "User doesn't exist"
                print(message)
                return render(request, "message.html", {'msg': message})
        else:
            job = JobDetails.objects.get(id=pk)
            print(f"Job retrieved for GET request: {job}")
            return render(request, "job-form.html", {"job": job})
    except Exception as e:
        print("Error:", e)
        return render(request, "error.html", {'error': str(e)})

def AppliedJobs(request):
    try:
        user_id = request.session.get('user_id')
        if user_id:
            
            can = Candidate.objects.get(user_id=user_id)
            ajobs = ApplyJob.objects.filter(candidate=can)
            return render(request, "apply_jobs.html", {'a_job': ajobs, 'user': user_id})
        else:
            return render(request, "message.html", {'msg': "User doesn't exist"})
    except Candidate.DoesNotExist:
        return render(request, "message.html", {'msg': "Candidate profile does not exist"})
    except Exception as e:
        print("Error:", e)
        return render(request, "error.html", {'error': str(e)})

        

''' company side views start here '''

def CompanyPage(request):
    user = request.session.get("user_id")
    if user:
        comp = Company.objects.get(user_id=user)
        return render(request, "company templates/index.html", {"user": user, "comp": comp})
    else:
        return render(request, " company templates/message.html", {'msg': "User doesn't exist"})



def Com_profile(request,pk):
    user=UserMaster.objects.get(pk=pk)
    com=Company.objects.get(user_id=user)
    return render(request,"company templates/cprofile.html",{'com':com,'user':user})

def Com_Update_profile(request,pk):
    try:
        if request.method == "POST":
            print("POST Data:", request.POST)
            user = UserMaster.objects.get(pk=pk)
            if user.role == "Company":
                com = Company.objects.get(user_id=user)
                com.contact = request.POST.get('contact', com.contact)
                com.city = request.POST.get('city',com.city)
                com.address = request.POST.get('address',com.address)
                com.state = request.POST.get('state',com.state)              
                com.website = request.POST.get('website',com.website)
                com.company_name = request.POST.get('name',com.company_name)
                com.description = request.POST.get('desc', com.description)

                if 'logo_pic' in request.FILES:
                    com.logo_pic = request.FILES['logo_pic']
                    print("logo pic uploaded:", request.FILES['logo_pic'])
                else:
                    print("No logo pic in request.FILES")

                com.save()
                print("Profile saved:", com.logo_pic.url if com.logo_pic else "No logo pic")
                url = f'/companyprofile/{pk}'
                return redirect(url)
            else:
                return render(request, "company templates/index.html", {'pk': pk})
    except UserMaster.DoesNotExist:
        print("UserMaster.DoesNotExist")
        return render(request, "company templates/404.html")
    except Company.DoesNotExist:
        print("User DoesNotExist")
        return render(request, "company templates/404.html")
    except Exception as e:
        print("Error:", e)
        return render(request, "error.html", {'error': str(e)})
    
   
def JobPage(request):
    return render(request,'company templates/jobpost.html')

def Post_Job(request):
    try:
        if request.method == "POST":#checking the method of post or not
            print("POST Data:", request.POST)#it is not necessary but to know the data used it
            user_id = request.session.get('user_id')  # Retrieve user ID from session
            if not user_id:#if user is not present in the database
                return render(request, "login.html", {'msg': "Please log in first."})#it returns to the login page and gives a message
            user = UserMaster.objects.get(id=user_id)#getting the user data by using the usermaster model using the id as a variable
            if user.role == "Company":#if user.role is company if goes to the statements
                comp = Company.objects.get(user_id=user_id)  #it checks the user_id in the company model 
                jobname = request.POST.get('jname')
                c_name = request.POST.get('companyname')
                jobdesc = request.POST.get('jobdesc')
                qualification = request.POST.get('qualification')
                responsibilities = request.POST.get('responsibilities')
                location = request.POST.get('location')
                c_web = request.POST.get('website')
                cont = request.POST.get('contact')
                sal = request.POST.get('salary')
                exp = request.POST.get('experience')
                addr = request.POST.get('caddress')
                e_mail = request.POST.get('email')
                logo = request.FILES.get('image')  
                Shifts=request.POST.get('shift')
                deadline=request.POST.get('end_date')
                
                new_job = JobDetails.objects.create(#creating a new object and sending the data to the database(JobDetails)
                    company_id=comp,
                    job_name=jobname,
                    company_name=c_name,
                    company_address=addr,
                    job_description=jobdesc,
                    qualification=qualification,
                    responsibilities=responsibilities,
                    location=location,
                    company_website=c_web,
                    company_email=e_mail,
                    company_contact=cont,
                    salary=sal,
                    experience=exp,
                    logo=logo,
                    dead_line=deadline,
                    shifts=Shifts
                )
                message = "Successfully Posted The Job"#this is the message
                return render(request, 'company templates/message.html', {'msg': message})#it returns after the succesfull posting the job
            else:#if the above if statement is failed it goes to the else part
                message = "Failed To Post The Job"#this is the message
                return render(request, 'company templates/message.html', {'msg': message})#it returns the message page with a failed message
        else:#if the method is not post it goes to the else part
            return render(request, 'company templates/jobpost.html')#it reloads the page and goes to the post method or else it loads until the method as post
    except UserMaster.DoesNotExist:#this is the userdoesn't exist exception
        print("UserMaster.DoesNotExist")#this is a print statement with some data 
        return render(request, "company templates/404.html")#returns to the 404 error page
    except Company.DoesNotExist:#this is company doesn't exist exception
        print("Company.DoesNotExist")#a print statement
        return render(request, "company templates/404.html")#it returns the 404 error page
    except Exception as e:#this is the main exception if the above 2exceptions are not occurs then it show the error where occured
        print("Error:", e)#it prints in the terminal what the error is
        return render(request, "error.html", {'error': str(e)})#it shows the error in the error page 


def JobList(request):
    try:
        user_id = request.session.get('user_id')  # getting the user_id from the session 
        if not user_id:#if user not registered it return to login page
            return render(request, "login.html", {'msg': "Please log in first."})#it returns with a message in the login page

        user = UserMaster.objects.get(id=user_id)#getting the details from the usermaster details from the database
        print("User:", user)#print the user details not mandetory

        company = Company.objects.get(user_id=user)#getting the details from the company data base using user
        print("Company:", company)#printing the company id

        company_jobs = JobDetails.objects.filter(company_id=company)#getting the data from the jobdetails model
        return render(request, "company templates/joblist.html", {'jobs': company_jobs})#it returns the data in the jobs details page 
    except UserMaster.DoesNotExist:#exception id user is not in the usermaster model
        print(f"User with ID {user_id} does not exist.")#prints the userid with a message 
        return render(request, "company templates/404.html")#it returns to the 404 error page 
    except Company.DoesNotExist:#exception id company id is not in the company model
        print(f"No Company found for user ID: {user_id}")#prints the data where user is not existed
        message = "Company is not registered. Please create a company profile first."#this is the message that returns in the error page
        return render(request, "error.html", {'error': message})#returning in the error page with a message
    except Exception as e:#exception is used in this exception in case above the exception are not occurs
        print("Error:", e)#it shows in the terminal
        return render(request, "error.html", {'error': str(e)})#it returns to error page and shows the error where it occurs
    
def A_list(request):
    try:
        user_id=request.session.get("user_id")
        if user_id:
            user=UserMaster.objects.get(id=user_id)
            comp=Company.objects.get(user_id=user)
            com_jobs=JobDetails.objects.filter(company_id=comp)
            a_jobs=ApplyJob.objects.filter(job__in=com_jobs)
            return render(request,"company templates/applied_lists.html",{"ajob":a_jobs})
        else:
            return render(request, "login.html", {'msg': "Please log in first."})
    except UserMaster.DoesNotExist:
        return render(request,"404.html")
    except Company.DoesNotExist:
        return render(request,"404.html")
    except JobDetails.DoesNotExist:
        return render(request,"404.html")
    except ApplyJob.DoesNotExist:
        return render(request,"404.html")
    except Exception as e:
        return render(request,"error.html",{'error':str(e)})
    
def Contact_us(request):
    return render(request, "company templates/contact.html")

def ContactQuery(request):
    try:
        if request.method == 'POST':
            print("POST request received")  # Debug statement
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # Debug statements to check received data
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Subject: {subject}")
            print(f"Message: {message}")

            new_query = Queries.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            print("New query created")  # Debug statement
            new_query.save()
            print("New query saved")  # Debug statement

            return render(request,"company templates/message.html",{'msg':"Successfully posted the query"})
        else:
            print("GET request received")  # Debug statement
            return render(request, "company templates/contact.html")
    except Exception as e:
        print("Error:", e)  # Debug statement
        return render(request, "error.html", {'error': str(e)})
