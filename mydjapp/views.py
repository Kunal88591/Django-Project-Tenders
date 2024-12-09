from django.shortcuts import render , redirect
from . import models
from . import emailAPI
import time

#middleware to check session for mainapp routes
def sessioncheck_middleware(get_response):
	def middleware(request):
		if request.path=='/home/' or request.path=='/about/' or request.path=='/contact/' or request.path=='/login/' or request.path=='/service/' or request.path=='/register/':
			request.session['sunm']=None
			request.session['srole']=None
			response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware


def home(request):
    return render(request,"home.html")    

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def service(request):
    return render(request,"service.html")

def register(request):
    if request.method=="GET":
        return render(request,"register.html",{"output":""})
    else:
        #to recieve data from form component
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        mobile=request.POST.get("mobile")
        address=request.POST.get("address")
        city=request.POST.get("city")
        gender=request.POST.get("gender")
        
        #to send verification email
        emailAPI.sendMail(email,password)

        #insert record using models
        p=models.Register(name=name,email=email,password=password,mobile=mobile,address=address,city=city,gender=gender,status=0,role="user",info=time.asctime())
        p.save()

        return render(request,"register.html",{"output":"User register successfully...."})                

def verify(request):
    vemail=request.GET.get("vemail")    
    models.Register.objects.filter(email=vemail).update(status=1)
    return redirect("/login/")

def login(request):
    if request.method=="GET":
        return render(request,"login.html",{"output":""})
    else:
        #to recieve data from form component
        email=request.POST.get("email")
        password=request.POST.get("password")

        #to check user is valid or not
        users=models.Register.objects.filter(email=email,password=password,status=1)

        #to check users & redirect accordingly
        if len(users)>0:      

            #to store user details in session
            request.session["sunm"]=users[0].email
            request.session["srole"]=users[0].role

            if users[0].role=="user":
                return redirect("/user/")
            else:
                return redirect("/myadmin/")            
        else:            
            return render(request,"login.html",{"output":"Invalid user or verify your account...."})    


