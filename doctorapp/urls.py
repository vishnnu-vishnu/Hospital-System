from django.urls import path
from doctorapp import views

urlpatterns = [
    path('doctorhome/',views.doctorhome,name="doctorhome"),
    path('doctorlogin/',views.doctorlogin,name="doctorlogin"),
    path('logindoctor/',views.logindoctor,name="logindoctor"),
    path('otp_verification/',views.otp_verification,name="otp_verification"),
    path('otps_verification/',views.otps_verification,name="otps_verification"),
    path('viewappointments/', views.viewappointments, name='viewappointments'),
    path('doctorlogout/', views.doctorlogout, name='doctorlogout'),
    path('leaveapply/', views.leaveapply, name='leaveapply'),
    path('leavesave/', views.leavesave, name='leavesave'),
    path('leavestatus/', views.leavestatus, name='leavestatus'),
    path('profilepage/', views.profilepage, name='profilepage'),
    path('updateappointment/<int:dataid>/',views.updateappointment,name="updateappointment"),
    path('patienthistory/<int:userid>/',views.patienthistory,name="patienthistory"),
    path('doctoredit/<int:dataid>/',views.doctoredit,name="doctoredit"),
    path('updatedoctoredit/<int:dataid>/',views.updatedoctoredit,name="updatedoctoredit"),
    path('doctorchangepassword/',views.doctorchangepassword,name="doctorchangepassword"),
    path('update_doctor_change_password/',views.update_doctor_change_password,name="update_doctor_change_password"),
]