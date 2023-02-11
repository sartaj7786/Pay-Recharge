from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
from flexy.models import Contact 
from flexy.models import Addrecharge
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")
    # return HttpResponse("This is the Mobile Rechage Shop")

def about(request):
     return render(request,"about.html")
    
    

def contact(request):
      if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date= datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent!')

      return render(request, 'contact.html')
    
   
    

def addrecharge(request):
     print("Recharge done")
     if request.method == "POST":
        phone = request.POST.get('phone ') 
        amount = request.POST.get('amount')
        operator = request.POST.get('operator')
        desc = request.POST.get('desc')
        addrecharge = Addrecharge(phone=phone,amount=amount,operator=operator,desc=desc, date=datetime.today())
        addrecharge.save()
        messages.success(request, 'Your Message has been sent!')
     return render(request,'addrecharge.html')
           
def signup(request):
    # print("i am running")
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password != confirm_password:
            return HttpResponse("password incorrect")
            return render(request,'/signup.html/')
        try:
            if User.objects.get(username=email):
                return  HttpResponse("email already exist")
               
        except Exception as identifier:
            pass
        user=User.objects.create_user(email,email,password)
        user.save()
        return HttpResponse("User created",email)

    return render(request,"signup.html")
       # print("i am runing the signup function")
    # if(request.method=="POST"):
    #     print("it i post request")
    # else:
    #     print("it is get request")

def handlelogin(request):
    return render(request,"login.html")
    
def handlelogout(request):
    return redirect("login")          