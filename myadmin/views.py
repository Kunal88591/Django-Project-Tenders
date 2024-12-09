from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from . import models
from mydjapp import models as mydjapp_models

#middleware to check session for admin routes
def sessioncheckmyadmin_middleware(get_response):
	def middleware(request):
		if request.path=='/myadmin/' or request.path=='/myadmin/manageusers/' or request.path=='/myadmin/manageuserstatus/' :
			if request.session['sunm']==None or request.session['srole']!="admin":
				response = redirect('/login/')
			else:
				response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware



#Create your views here.
def adminhome(request):
 return render(request,"adminhome.html",{"sunm":request.session["sunm"]})

def manageusers(request):
 usersList=mydjapp_models.Register.objects.filter(role="user")   
 print(usersList)
 return render(request,"manageusers.html",{"usersList":usersList,"sunm":request.session["sunm"]}) 

def manageuserstatus(request):
 s=request.GET.get("s")    
 regid=int(request.GET.get("regid"))

 if s=="block":
  mydjapp_models.Register.objects.filter(regid=regid).update(status=0)       
 elif s=="verify":
  mydjapp_models.Register.objects.filter(regid=regid).update(status=1)    
 else:
  mydjapp_models.Register.objects.filter(regid=regid).delete();      

 return redirect("/myadmin/manageusers/")

def epadmin(request):
 sunm=request.session["sunm"]
 if request.method=="GET":	
  userDetails=mydjapp_models.Register.objects.filter(email=sunm)		
  m,f="",""
  if userDetails[0].gender=="male":
    m="checked"
  else:
    f="checked"
  return render(request,"epadmin.html",{"sunm":request.session["sunm"],"userDetails":userDetails[0],"output":"","m":m,"f":f})
 else:
  name=request.POST.get("name")
  mobile=request.POST.get("mobile")
  address=request.POST.get("address")
  city=request.POST.get("city")
  gender=request.POST.get("gender")

  mydjapp_models.Register.objects.filter(email=sunm).update(name=name,mobile=mobile,address=address,city=city,gender=gender)

  return redirect("/myadmin/epadmin/")    	 

def cpadmin(request):
 if request.method=="GET":	
  return render(request,"cpadmin.html",{"sunm":request.session["sunm"],"output":""})
 else:
  sunm=request.session["sunm"]
  opass=request.POST.get("opass")
  npass=request.POST.get("npass")
  cnpass=request.POST.get("cnpass")		

  userDetails=mydjapp_models.Register.objects.filter(email=sunm,password=opass)
  
  if len(userDetails)>0:
   if npass==cnpass:
    mydjapp_models.Register.objects.filter(email=sunm).update(password=cnpass)
    return render(request,"cpadmin.html",{"sunm":sunm,"output":"Password changed successfully"})
   else:
    return render(request,"cpadmin.html",{"sunm":sunm,"output":"New & Confirm new password mismatch"})	 		
  else:
   return render(request,"cpadmin.html",{"sunm":sunm,"output":"Invalid old password"})    

def addcategory(request):
 if request.method=="GET":    
  return render(request,"addcategory.html",{"output":"","sunm":request.session["sunm"]})
 else:
  catname=request.POST.get("catname")
  caticon=request.FILES["caticon"]
  fs = FileSystemStorage()
  filename = fs.save(caticon.name,caticon)
  p=models.Category(catname=catname,caticonname=filename)
  p.save()
  return render(request,"addcategory.html",{"output":"Category added successfully....","sunm":request.session["sunm"]})

def addsubcategory(request):
 clist=models.Category.objects.all()  
 if request.method=="GET":    
  return render(request,"addsubcategory.html",{"clist":clist,"sunm":request.session["sunm"],"output":""})
 else:
  catname=request.POST.get("catname")
  subcatname=request.POST.get("subcatname")
  caticon=request.FILES["caticon"]
  fs = FileSystemStorage()
  filename = fs.save(caticon.name,caticon)
  p=models.SubCategory(catname=catname,subcatname=subcatname,subcaticonname=filename)
  p.save()
  return render(request,"addsubcategory.html",{"clist":clist,"sunm":request.session["sunm"],"output":"Subcategory added successfully...."})

