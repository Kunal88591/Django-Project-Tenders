from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from . import models
from myadmin import models as myadmin_models

import time

MEDIA_URL=settings.MEDIA_URL

#middleware to check session for user routes
def sessioncheckuser_middleware(get_response):
	def middleware(request):
		if request.path=='/user/' :
			if request.session['sunm']==None or request.session['srole']!="user":
				response = redirect('/login/')
			else:
				response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware


#Create your views here.
def userhome(request):
 return render(request,"userhome.html",{"sunm":request.session["sunm"]})

def viewcategory(request):
 clist=myadmin_models.Category.objects.all()	
 return render(request,"viewcategory.html",{"clist":clist,"MEDIA_URL":MEDIA_URL,"sunm":request.session["sunm"]})

def viewsubcategory(request):
 catname=request.GET.get("catname")
 sclist=myadmin_models.SubCategory.objects.filter(catname=catname)	
 return render(request,"viewsubcategory.html",{"catname":catname,"sclist":sclist,"MEDIA_URL":MEDIA_URL,"sunm":request.session["sunm"]})

def viewtender(request):
 subcatname=request.GET.get("subcatname")
 tlist=models.Tender.objects.filter(subcatname=subcatname)	
 return render(request,"viewtender.html",{"subcatname":subcatname,"tlist":tlist,"MEDIA_URL":MEDIA_URL,"sunm":request.session["sunm"]}) 

def tendermain(request):
 tenderid=int(request.GET.get("tenderid"))
 t=models.Tender.objects.filter(tenderid=tenderid)	
 return render(request,"tendermain.html",{"t":t[0],"MEDIA_URL":MEDIA_URL,"sunm":request.session["sunm"]}) 

def funds(request):
 paypalURL="https://www.sandbox.paypal.com/cgi-bin/webscr"
 paypalID="sb-okfnc32273845@business.example.com"    
 amt=100
 return render(request,"funds.html",{"paypalID":paypalID,"paypalURL":paypalURL,"amt":amt,"sunm":request.session["sunm"]})

def payment(request):
 uid=request.GET.get("uid")
 amt=request.GET.get("amt")  
 p=models.Funds(uid=uid,amt=int(amt),info=time.asctime())
 p.save()
 return redirect("/user/success/")

def success(request):
 return render(request,"success.html",{"sunm":request.session["sunm"]})

def cancel(request):
 return render(request,"cancel.html",{"sunm":request.session["sunm"]})


def addtender(request):
 sclist=myadmin_models.SubCategory.objects.all()	
 if request.method=="GET":	
  return render(request,"addtender.html",{"sunm":request.session["sunm"],"sclist":sclist,"output":""})
 else:
  title=request.POST.get("title")
  subcatname=request.POST.get("subcatname")
  description=request.POST.get("description")
  sdate=request.POST.get("sdate")
  edate=request.POST.get("edate")

  tenderfile=request.FILES["tenderfile"]
  fs = FileSystemStorage()
  filename = fs.save(tenderfile.name,tenderfile)
  p=models.Tender(title=title,subcatname=subcatname,description=description,sdate=sdate,edate=edate,tenderfilename=filename,uid=request.session["sunm"],info=time.asctime())
  p.save()  	
  return render(request,"addtender.html",{"sunm":request.session["sunm"],"sclist":sclist,"output":"Tender added successfully...."})    	  

