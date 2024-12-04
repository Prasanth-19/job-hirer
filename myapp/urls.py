from django.urls import path
from . import views



    
urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("otps/",views.otps,name="otpcheck"),
    path("Index-contact",views.cus,name="index-cs"),
    path("Index-message",views.Contactquery,name="index-message"),
    path("about/",views.Aboutus,name="about"),
    path("canidate-contact/",views.Contact,name="contact"),
    path("candidate-queries/",views.Contact_query,name="contactus"),
    path("signup/",views.SignupPage,name="signup"),
    path("register/",views.RegisterUser,name="register"),
    path("otp-verify",views.OtpVerify,name="otpVerify"),
    path("otp/<str:email>/",views.OtpVerification,name="otpVerification"),
    path("loginpage/",views.loginPage,name="loginpage"),
    path("login/",views.LoginUser,name="login"),
    path("logout/",views.logout_page,name="logout"),
    path("terms/",views.TermsAndConditions,name="terms"),
    path("otp-resend/<str:email>/",views.ResendOtp,name="resendotp"),
    path("forgot-password/",views.ForgotPassword,name="forgot_password"),
    path("verify-otp/",views.VerifyOtp,name="verify_otp"),
    path("candidatepage/",views.CandidatePage,name="cpage"),
    path("profilepage/<int:pk>/",views.ProfilePage,name="profilepage"),
    path("updateprofile/<int:pk>/",views.UpdateProfile,name="uprofile"),
    path("job-lists/",views.Job_List,name="joblist"),
    path("jobdetails/<int:pk>/",views.Job_Details,name="j_details"),
    path("job-form/<int:pk>/",views.Job_ApplyPage,name="j_form"),
    path("job-apply/<int:pk>/",views.Apply_Job,name="j_apply"),
    path("jobs-applied/",views.AppliedJobs,name="j_applied"),

    
    
    # company side starts here #
    path("companypage/",views.CompanyPage,name="compage"),
    path("companyprofile/<int:pk>/",views.Com_profile,name="cprofile"),
    path("c-updateprofile/<int:pk>/",views.Com_Update_profile,name="comup"),
    path("jobpage/",views.JobPage,name='jpage'),
    path("postjob/",views.Post_Job,name="jpost"),
    path("job_list/",views.JobList,name="jlist"),
    path("applied-list/",views.A_list,name="a_list"),
    path("company-contact_us/",views.Contact_us,name="c_us"),
    path("company-contact/query/",views.ContactQuery,name="c_query"),
]
