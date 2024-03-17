from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from backend.models import categorydb, departmentdb, profiledb,doctordb
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages
from frontend.models import appointmentdb,contactdb
from django.utils import timezone
from django.http import HttpResponse
from doctorapp.models import applyleavedb
from django.core.mail import send_mail
from datetime import date


# Create your views here.

def indexfun(request):
    return render(request, "index.html")


def addcat(request):
    return render(request, "add_category.html")


def adddept(request):
    categ = categorydb.objects.all()
    return render(request, "add_department.html", {'categ': categ})


def savecat(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        cd = request.POST.get('cdes')
        obj = categorydb(catname=cn, catdes=cd)
        obj.save()
        messages.success(request,"Saved Category Sucessfully")
        return redirect(addcat)


def displaycat(request):
    data = categorydb.objects.all()
    return render(request, "display_category.html", {'data': data})


def editcat(request, dataid):
    cat = categorydb.objects.get(id=dataid)
    return render(request, "edit_category.html", {'cat': cat})


def updatecat(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('cname')
        cd = request.POST.get('cdes')
        categorydb.objects.filter(id=dataid).update(catname=cn, catdes=cd)
        messages.success(request, "Updated Category Sucessfully")
        return redirect(displaycat)


def deletecat(request, dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    messages.error(request, "Deleted Category Sucessfully")
    return redirect(displaycat)


def savedep(request):
    if request.method == "POST":
        dn = request.POST.get('dname')
        dc = request.POST.get('dcat')
        ds = request.POST.get('ddes')
        di = request.FILES['dimg']
        obj = departmentdb(depname=dn, depcat=dc, depdes=ds, depimg=di)
        obj.save()
        messages.success(request, "Saved Department Sucessfully")
        return redirect(adddept)


def displaydepartment(request):
    data = departmentdb.objects.all()
    return render(request, "display_department.html", {'data': data})


def editdepartment(request, dataid):
    cat = categorydb.objects.all()
    data = departmentdb.objects.get(id=dataid)
    return render(request, "edit_department.html", {'data': data, 'cat': cat})


def updatedepartment(request, dataid):
    if request.method == "POST":
        dn = request.POST.get('dname')
        dc = request.POST.get('dcat')
        ds = request.POST.get('ddes')
        try:
            img = request.FILES['dimg']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = departmentdb.objects.get(id=dataid).depimg
        departmentdb.objects.filter(id=dataid).update(depname=dn, depcat=dc, depdes=ds, depimg=file)
        messages.success(request, "Updated Department Sucessfully")
        return redirect(displaydepartment)

def deletedepartment(request,dataid):
    dele=departmentdb.objects.filter(id=dataid)
    dele.delete()
    messages.error(request, "Delete Department Sucessfully")
    return redirect(displaydepartment)

def admin_login(request):
    return render(request,"adminlogin.html")

def adminlogin(request):
    if request.method == "POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(indexfun)
            else:
                messages.error(request, "Invalid Login")
                return redirect(admin_login)
        else:
            messages.error(request, "Invalid Login")
            return redirect(admin_login)


def profile(request):
    data=profiledb.objects.all()
    return render(request,"profile.html",{'data':data})

def editprofile(request):

    return render(request,"editprofile.html")

def saveprofile(request):
    if request.method == "POST":
        na=request.POST.get('name')
        un=request.POST.get('username')
        em=request.POST.get('email')
        mo=request.POST.get('mobile')
        ad=request.POST.get('address')
        pc=request.POST.get('po')
        st=request.POST.get('state')
        im=request.FILES['img']
        obj=profiledb(pname=na,uname=un,pmail=em,pmobile=mo,paddress=ad,pcode=pc,pstate=st,pimage=im)
        obj.save()
        return redirect(profile)


def updateprofile(request,dataid):
    if request.method == "POST":
        na=request.POST.get('name')
        un=request.POST.get('username')
        em=request.POST.get('email')
        mo=request.POST.get('mobile')
        ad=request.POST.get('address')
        pc=request.POST.get('po')
        st=request.POST.get('state')
        try:
            img = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = profiledb.objects.get(id=dataid).pimage
        profiledb.objects.filter(id=dataid).update(pname=na,uname=un,pmail=em,pmobile=mo,paddress=ad,pcode=pc,pstate=st,pimage=file)
        return redirect(profile)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

def adddoctor(request):
    data=departmentdb.objects.filter()
    return render(request,"adddoctor.html",{'data':data})

def doctorsave(request):
    if request.method=="POST":
        dn=request.POST.get('dname')
        ds=request.POST.get('special')
        qu=request.POST.get('qual')
        pf=request.POST.get('profile')
        de=request.POST.get('email')
        dm=request.POST.get('number')
        dg=request.POST.get('gender')
        df=request.POST.get('fee')
        di=request.POST.get('doctorid')

        if doctordb.objects.filter(doctorid=di).exists():
            return HttpResponse("Doctor with this ID already exists.")

        obj=doctordb(dname=dn,special=ds,dmail=de,dphone=dm,gender=dg,fee=df,qualification=qu,profile=pf,doctorid=di)
        obj.save()

        send_verification_email(di, de, obj.generate_password(), dn)

    return redirect(adddoctor)

def send_verification_email(doctorid, email, password,doctor_name):
    subject = f'Doctor Verification - {doctorid}'
    message = f'Dear {doctor_name},\n\nThank you for registering. Your account has been verified.\n\nDoctor ID: {doctorid}\nPassword: {password}\n\nSincerely,\nYour Hospital Team'
    from_email = 'vishnumampattakunnath@gmail.com'  # Update with your email
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

def displaydoctor(request):
    data=doctordb.objects.all()
    return render(request,"displaydoctor.html",{'data':data})

def deletedoctor(request,dataid):
    data=doctordb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydoctor)



def editdoctor(request,dataid):
    datas=doctordb.objects.get(id=dataid)
    cat = categorydb.objects.all()
    data = departmentdb.objects.all()
    return render(request,"editdoctor.html",{'datas':datas,'cat':cat,'data':data})

def updatedoctor(request,dataid):
    if request.method=="POST":
        dn = request.POST.get('dname')
        ds = request.POST.get('special')
        qu = request.POST.get('qual')
        pf = request.POST.get('profile')
        de = request.POST.get('email')
        dm = request.POST.get('number')
        dg = request.POST.get('gender')
        df = request.POST.get('fee')
        doctordb.objects.filter(id=dataid).update(dname=dn, special=ds, dmail=de, dphone=dm, gender=dg, fee=df,qualification=qu,profile=pf)
        return redirect(displaydoctor)



def appliedleave(request):
    data=applyleavedb.objects.all()
    a='Approved'
    cat=applyleavedb.objects.filter(status=a)
    return render(request,"appliedleave.html",{'data':data,'cat':cat})

def displaycontact(request):
    data=contactdb.objects.all()
    return render(request,"displaycontact.html",{'data':data})
def sendmessage(request,dataid):
    cat=contactdb.objects.get(id=dataid)
    return render(request,"sendmessage.html",{'cat':cat})

def sendreply(request,dataid):
    if request.method=="POST":
        em=request.POST.get('email')
        me=request.POST.get('rmes')
        contactdb.objects.filter(id=dataid).update(reply=me)

        subject = 'Care Plus Team'
        message = f'{me}'
        from_email = 'your_email@example.com'  # Replace with your email address
        recipient_list = [em]  # Use the entered email address as the recipient

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return redirect(displaycontact)

    return render(request, 'error_page.html',{'message_sent': False})

def updatestatus(request,dataid):
    if request.method=="POST":
        s=request.POST.get('approve')
        applyleavedb.objects.filter(id=dataid).update(status=s)
        return redirect(appliedleave)

def appointmentlist(request):
    data=appointmentdb.objects.filter(status='Pending',date=date.today())
    user=appointmentdb.objects.filter(status='Completed',date=date.today())

    return render(request,"appointments.html",{'data':data,'user':user})


def patientcontact(request,dataid):
    data=appointmentdb.objects.get(bookingid=dataid)
    return render(request,"contactpatient.html",{'data':data})

def patientreply(request,dataid):
    if request.method=="POST":
        em=request.POST.get('email')
        me=request.POST.get('rmes')

        subject = 'Care Plus Team'
        message = f'{me}'
        from_email = 'your_email@example.com'  # Replace with your email address
        recipient_list = [em]  # Use the entered email address as the recipient

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return redirect(appointmentlist)

    return render(request, 'error_page.html',{'message_sent': False})

def pateintprofile(request,userid):
    data=appointmentdb.objects.filter(userid=userid)
    return render(request,"patientprofile.html",{'data':data})

def opening(request):
    return render (request,"opening.html")



