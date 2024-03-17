from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from datetime import date
import random
from doctorapp.models import applyleavedb
from backend.models import doctordb, profiledb
from frontend.models import appointmentdb,userdb

from django.contrib.auth.decorators import login_required
from doctorapp.models import DoctorAttendance




def doctorhome(request):
    return render(request,"doctorhome.html")

def doctorlogin(request):
    return render(request,"doctorlogin.html")

def otp_verification(request):
    return render(request,"otp_verification.html")


# otp generating
def generate_otp():
    return str(random.randint(100000, 999999))



# for send otp
def send_otp(user_id,otp):
    try:
        doctor=doctordb.objects.get(doctorid=user_id)
        to=str(doctor.dmail)
        subject = 'OTP - JobFinder'
        message = f'Dear {doctor.dname},\n\nYour OTP for login is: {otp}'
        from_email = 'your_email@example.com'

        send_mail(subject, message, from_email, [to], fail_silently=False)

    except doctordb.DoesNotExist:
        print(f"User with email {user_id} not found.")


def logindoctor(request):
    if request.method=="POST":
        user_id=request.POST.get('userid')
        pwd=request.POST.get('password')
        na=request.POST.get('name')
        if doctordb.objects.filter(doctorid=user_id,password=pwd,dname=na).exists():
            otp=generate_otp()

            try:
                send_otp(user_id,otp)
                request.session['otp']=otp
                request.session['doctorid']=user_id
                request.session['dname']=na
                request.session['password']=pwd
                return redirect(otp_verification)
            except Exception as e:
                messages.error(request,f"Error Sending OTP:{e}")
                return redirect(doctorlogin)
        else:
            return render(request,"doctorlogin.html")
    return render(request,"doctorlogin.html")







def otps_verification(request):
    if request.method=="POST":
        userentered_otp=request.POST.get('otp')
        stored_otp=request.session.get('otp')

        if userentered_otp==stored_otp:
            return redirect(doctorhome)
        else:
            incorrect_otp_alert = True
            return render(request,"otp_verification.html",{'incorrect_otp_alert':incorrect_otp_alert})
    else:
        generated_otp = send_otp()
        request.session['otp'] = generated_otp
        return render(request,"otp_verification.html")

def doctorlogout(request):
    del request.session['doctorid']
    del request.session['dname']
    del request.session['password']
    return redirect(doctorlogin)


def viewappointments(request):
    data=appointmentdb.objects.filter(doctor=request.session['dname'],status='Pending',date=date.today())
    cat=appointmentdb.objects.filter(doctor=request.session['dname'],status='Completed',date=date.today())

    return render(request,"viewappointments.html",{'data':data,'cat':cat})

def updateappointment(request,dataid):
    if request.method=="POST":
        st=request.POST.get('status')
        re=request.POST.get('remarks')
        appointmentdb.objects.filter(bookingid=dataid).update(status=st,remarks=re)
        return redirect(viewappointments)


def leaveapply(request):
    return render(request,"leaveapply.html")


def leavesave(request):
    if request.method=="POST":
        na=request.POST.get('name')
        fr=request.POST.get('from')
        ot=request.POST.get('to')
        le=request.POST.get('leave')
        re=request.POST.get('reason')
        obj=applyleavedb(name=na,fromdate=fr,todate=ot,leave=le,reason=re)
        obj.save()
        return redirect(leavestatus)

def leavestatus(request):
    data=applyleavedb.objects.filter(name=request.session['dname'])
    return render(request,"leavestatus.html",{'data':data})


def profilepage(request):
    data=doctordb.objects.filter(dname=request.session['dname'])
    return render(request,"profilepage.html",{'data':data})

def patienthistory(request,userid):
    user_data = appointmentdb.objects.filter(userid=userid)
    return render(request,"patienthistory.html",{'user_data':user_data})

def doctoredit(request,dataid):
    user=doctordb.objects.get(id=dataid)
    return render(request,"doctoredit.html",{'user':user})

def updatedoctoredit(request,dataid):
    if request.method == "POST":
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        location = request.POST.get('location')
        address = request.POST.get('address')
        try:
            img = request.FILES['profile']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = doctordb.objects.get(id=dataid).profileimage
        doctordb.objects.filter(id=dataid).update( age=age, dob=dob, profileimage=file,address=address,qualification=qualification,Experiance=experience,Location=location)
        return redirect(profilepage)


def doctorchangepassword(request):
    return render(request,"doctorchangepassword.html")

def update_doctor_change_password(request):
    if request.method=="POST":
        o=request.POST.get('old')
        n=request.POST.get('new')
        user = doctordb.objects.filter(dname=request.session['dname'], password=o).first()
        if user:
            user.password=n
            user.save()
            messages.success(request, 'Password successfully changed!')
            return redirect(profilepage)
        else:
            error_message=True
            return render(request, 'doctorchangepassword.html', {'error_message':error_message})
    return render(request, 'doctorchangepassword.html')


