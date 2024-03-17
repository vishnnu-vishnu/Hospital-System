from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse
from datetime import datetime


from backend.models import departmentdb,categorydb,doctordb
from frontend.models import appointmentdb,contactdb,userdb
from doctorapp.models import applyleavedb
from django.core.mail import send_mail


# Create your views here.
today_date = datetime.now().date()




def homepage(request):
    dep=categorydb.objects.all()
    user=userdb.objects.filter(email=request.session['email'])
    return render(request,"home.html",{'dep':dep,'user':user})
def department(request,depo):
    dep = categorydb.objects.all()
    data=departmentdb.objects.filter(depcat=depo)
    return render(request,"deaprtment.html",{'data':data,'dep':dep})

def contact(request):
    dep = categorydb.objects.all()
    return render(request,"contact.html",{'dep':dep})
def about(request):
    dep = categorydb.objects.all()
    return render(request,"about.html",{'dep':dep})

def singledep(request,dataid):
    data=departmentdb.objects.get(id=dataid)
    dep = categorydb.objects.all()
    return render(request,"singledepartment.html",{'data':data,'dep':dep})
def doctor(request):
    data=doctordb.objects.all()
    dep = categorydb.objects.all()
    cat = applyleavedb.objects.filter(status="Approved", fromdate=today_date)
    return render(request,"doctors.html",{'data':data,'dep':dep,'cat':cat})
def docpro(request,datasid):
    datad=doctordb.objects.get(id=datasid)
    dep = categorydb.objects.all()
    return render(request,"doctorprofile.html",{'datad':datad,'dep':dep})

def filterdoctor(request,depa):
    cat = doctordb.objects.all()
    datad = doctordb.objects.filter(special=depa)
    dep = categorydb.objects.all()
    return render(request,"filterdoctor.html",{'datad':datad,'cat':cat,'dep':dep})

def appointment(request):
    data=doctordb.objects.all()
    dep = categorydb.objects.all()
    user=userdb.objects.filter(email=request.session['email'])
    return render(request,"appointment.html",{'data':data,'dep':dep,'user':user})

def saveappointment(request):
    if request.method=="POST":
        fn=request.POST.get('firstname')
        ln=request.POST.get('lastname')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        de=request.POST.get('department')
        do=request.POST.get('doctor')
        da=request.POST.get('date')
        co=request.POST.get('consultation')
        ad=request.POST.get('address')
        me=request.POST.get('message')
        ag=request.POST.get('age')
        gn=request.POST.get('gender')
        ui=request.POST.get('userid')
        obj=appointmentdb(firstname=fn,lastname=ln,email=em,phone=ph,department=de,doctor=do,date=da,consultation=co,address=ad,message=me,age=ag,gender=gn,userid=ui)
        obj.save()
        booking_id = obj.bookingid

        subject='ThankYou For Making Appointment'
        message=f'Dear {fn}{ln} Thank You For Making Appiontment \n Herewith Attaching your booking slip '
        from_email = 'your_email@example.com'
        recipient_list=[em]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)


        data={'fn':fn,'ln':ln,'em':em,'ph':ph,'de':de,'do':do,'da':da,'ag':ag,'gn':gn,'booking_id':booking_id}
        return render(request,"pdf.html",{'data':data})
    return render(request,"appointment.html")

def pdf(request):
    return render(request,"pdf.html")

def savecontact(request):
    if request.method=="POST":
        na=request.POST.get('name')
        mo=request.POST.get('mobile')
        em=request.POST.get('email')
        me=request.POST.get('message')
        obj=contactdb(name=na,email=em,mobile=mo,message=me)
        obj.save()
        subject = 'Care Plus Team'
        message = f'Thankyou {na}for Your response ,Get in touch with you soon'
        from_email = 'your_email@example.com'  # Replace with your email address
        recipient_list = [em]  # Use the entered email address as the recipient

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return redirect(contact)  # Assuming 'contact' is the name of the URL pattern for the contact page

        # Handle cases where the request method is not POST
    return render(request, 'error_page.html')

def alldept(request):
    dep = categorydb.objects.all()
    results=departmentdb.objects.all()
    return render(request,"alldepartment.html",{'dep':dep,'results':results})

def searching(request):
    if request.method=="POST":
        query=request.POST.get('search')
        if query:
            results=departmentdb.objects.filter(depname__contains=query)
        else:
            results=[]
    return render(request,"alldepartment.html",{'results':results})


def usersignup(request):
    if request.method=="POST":
        uid=request.POST.get('userid')
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        address=request.POST.get('address')
        bloodgroup=request.POST.get('bloodgroup')
        obj=userdb(userid=uid,name=name,mobile=mobile,email=email,password=password,address=address,bloodgroup=bloodgroup)
        obj.save()
        return redirect(signinpage)
from django.contrib import messages

def usersignin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user exists with the given email and password
        user_exists = userdb.objects.filter(email=email, password=password).exists()

        if user_exists:
            request.session['email'] = email
            request.session['password'] = password
            return redirect('homepage')
        else:
            incorrectpass=True
            return render(request,'usersignin.html',{'incorrectpass':incorrectpass})

    return render(request, 'usersignin.html')


def signuppage(request):
    return render(request,"usersignup.html")

def signinpage(request):
    return render(request,"usersignin.html")

def userprofile(request):
    user=userdb.objects.filter(email=request.session['email'])
    return render(request,"userprofile.html",{'user':user})


def edituserprofile(request,dataid):
    user=userdb.objects.get(id=dataid)
    return render(request,"editprofile.html",{'user':user})


def updateprofile(request, dataid):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        blood = request.POST.get('blood')
        sex = request.POST.get('sex')
        address = request.POST.get('address')
        try:
            img = request.FILES['profile']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = userdb.objects.get(id=dataid).profile
        userdb.objects.filter(id=dataid).update(name=name, age=age, dob=dob, profile=file,bloodgroup=blood,sex=sex,address=address)
        return redirect(userprofile)




def logoutuser(request):
    del request.session['email']
    del request.session['password']
    return redirect(signinpage)

def changepassword(request):
    return render(request,"changepassword.html")

def updatepassword(request):
    if request.method=="POST":
        o=request.POST.get('old')
        n=request.POST.get('new')
        user = userdb.objects.filter(email=request.session['email'], password=o).first()
        if user:
            user.password=n
            user.save()

            request.session['password'] = n
            messages.success(request, 'Password successfully changed!')
            return redirect(userprofile)
        else:
            error_message=True
            return render(request, 'changepassword.html', {'error_message':error_message})
    return render(request, 'changepassword.html')







