from django.shortcuts import render,redirect,reverse
from .models import FileModel
from django.contrib import messages
import random
from datetime import datetime

# Create your views here.

def index(request):	
	return render(request,"index.html")

def exportFile(request):
	if request.method=="POST":
		files = FileModel.objects.all()

		code = request.POST.get("code")

		if len(code) == 0: 
			code = str(random.random())[2:8]

		for i in files:
			if i.spesificCode == code:
				messages.info(request,"The code is using, please create spesific one.")
				return redirect("exportFile")	    
		text = request.POST.get("text")
		lifetime = request.POST.get("customRadioInline1")
		if lifetime == None :
			lifetime = "oneday"
		if request.FILES:
			file = request.FILES["file"]

		model = FileModel(file=file,description=text,spesificCode=code,counter=0,lifetime=lifetime)
		model.save()
		messages.success(request,"File Exporting Successfully.")
		return redirect(reverse("exportInfo",kwargs={"code":code}))


	return render(request,"exportfile.html")

def importFile(request):
	if request.method == "POST":
		code = str(request.POST.get("code"))
		file = FileModel.objects.filter(spesificCode=code).first()
		if (file == None) or len(file.spesificCode) == 0:
			messages.warning(request,"Your code was not found.")
			return redirect("importFile")
		
		return redirect(reverse("file",kwargs={"code":code}))

	return render(request,"importfile.html")


def file(request,code):
	file = FileModel.objects.filter(spesificCode = code).first()
	lifetime = file.lifetime
	datetimes = str(file.exportDate)
	# Date Compute
	date = []
	date.append(int(datetimes[:4]))
	date.append(int(datetimes[5:7]))
	date.append(int(datetimes[8:10]))
	date.append(int(datetimes[11:13]))
	date.append(int(datetimes[14:16]))

	times = datetime.now() - datetime(date[0], date[1], date[2], date[3], date[4])

	#tenviews,onehundredviews,onekviews
	if lifetime == "tenviews":
		if file.counter >= 10 :
			file.delete()
			messages.warning(request,"This file has been deleted.")
			return redirect("index")
	elif lifetime == "onehundredviews":
		if file.counter >= 100 :
			file.delete()
			messages.warning(request,"This file has been deleted.")
			return redirect("index")
	elif lifetime == "onekviews":
		if file.counter >= 1000 :
			file.delete()
			messages.warning(request,"This file has been deleted.")
			return redirect("index")
				
	elif lifetime == "tenmins":
		if (times.seconds/60-60*3) >= 10:
			file.delete()
			messages.warning(request,"This file has been deleted.")
			return redirect("index")

	elif lifetime == "oneday":
		if (times.days) >= 1:
			file.delete()
			messages.warning(request,"This file has been deleted.")
			return redirect("index")


	elif lifetime == "tendays":
		if (times.days) >= 10:
			file.delete()
			messages.warning(request,"This file has been deleted.")
			return redirect("index")	

	file.counter += 1
	file.save()


	return render(request,"file.html",{"file":file})


def exportInfo(request,code):
    file = FileModel.objects.filter(spesificCode = code).first()
    return render(request,"exportinfo.html",{"file":file})
