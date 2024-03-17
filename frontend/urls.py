from django.urls import path
from frontend import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('department/<depo>/',views.department,name="department"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('filterdoctor/<depa>/',views.filterdoctor,name="filterdoctor"),
    path('doctor/',views.doctor,name="doctor"),
    path('pdf/',views.pdf,name="pdf"),
    path('appointment/',views.appointment,name="appointment"),
    path('saveappointment/',views.saveappointment,name="saveappointment"),
    path('docpro/<int:datasid>/',views.docpro,name="docpro"),
    path('singledep/<int:dataid>/',views.singledep,name="singledep"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('alldept/',views.alldept,name="alldept"),
    path('searching/',views.searching,name="searching"),
    path('usersignup/',views.usersignup,name="usersignup"),
    path('usersignin/',views.usersignin,name="usersignin"),
    path('signuppage/',views.signuppage,name="signuppage"),
    path('signinpage/',views.signinpage,name="signinpage"),

    path('userprofile/',views.userprofile,name="userprofile"),
    path('edituserprofile/<int:dataid>/',views.edituserprofile,name="edituserprofile"),
    path('updateprofile/<int:dataid>/',views.updateprofile,name="updateprofile"),
    path('logoutuser/', views.logoutuser, name="logoutuser"),
    path('changepassword/', views.changepassword, name="changepassword"),
    path('updatepassword/', views.updatepassword, name="updatepassword"),

]