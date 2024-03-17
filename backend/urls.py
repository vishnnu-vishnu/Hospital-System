from django.urls import path
from backend import views

urlpatterns = [
    path('indexfun/',views.indexfun,name="indexfun"),
    path('addcat/',views.addcat,name="addcat"),
    path('adddept/',views.adddept,name="adddept"),
    path('savecat/',views.savecat,name="savecat"),
    path('displaycat/',views.displaycat,name="displaycat"),
    path('editcat/<int:dataid>/',views.editcat,name="editcat"),
    path('updatecat/<int:dataid>/',views.updatecat,name="updatecat"),
    path('deletecat/<int:dataid>/',views.deletecat,name="deletecat"),
    path('savedep/',views.savedep,name="savedep"),
    path('displaydepartment/',views.displaydepartment,name="displaydepartment"),
    path('editdepartment/<int:dataid>/',views.editdepartment,name="editdepartment"),
    path('updatedepartment/<int:dataid>/',views.updatedepartment,name="updatedepartment"),
    path('deletedepartment/<int:dataid>/',views.deletedepartment,name="deletedepartment"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('profile/',views.profile,name="profile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('saveprofile/',views.saveprofile,name="saveprofile"),
    path('updateprofile/<int:dataid>/',views.updateprofile,name="updateprofile"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('adddoctor/',views.adddoctor,name="adddoctor"),
    path('doctorsave/',views.doctorsave,name="doctorsave"),
    path('editdoctor/<int:dataid>/',views.editdoctor,name="editdoctor"),
    path('displaydoctor/',views.displaydoctor,name="displaydoctor"),
    path('deletedoctor/<int:dataid>/',views.deletedoctor,name="deletedoctor"),
    path('updatedoctor/<int:dataid>/',views.updatedoctor,name="updatedoctor"),
    path('appliedleave/',views.appliedleave,name="appliedleave"),
    path('displaycontact/',views.displaycontact,name="displaycontact"),
    path('sendmessage/<int:dataid>/',views.sendmessage,name="sendmessage"),
    path('sendreply/<int:dataid>/',views.sendreply,name="sendreply"),
    path('updatestatus/<int:dataid>/',views.updatestatus,name="updatestatus"),
    path('appointmentlist/',views.appointmentlist,name="appointmentlist"),
    path('patientcontact/<int:dataid>/',views.patientcontact,name="patientcontact"),
    path('patientreply/<int:dataid>/',views.patientreply,name="patientreply"),
    path('pateintprofile/<int:userid>/',views.pateintprofile,name="pateintprofile"),
    path('',views.opening,name="opening"),



]