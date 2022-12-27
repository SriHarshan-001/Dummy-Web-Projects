from django.shortcuts import render
from securef.models import *



# Create your views here.
def intro(request):
    return render(request,"securef/front.html")


def adm(request):
    statement=""
    if request.method == "POST":
        username=request.POST.get("loginName")
        password=request.POST.get("loginPassword")
        a0=list(adminis.objects.values_list("username"))
        a1=list(adminis.objects.values_list("password"))
        for i in range(0,len(a0)):
            if (a0[i][0]==username and a1[i][0]==password):
                 return render(request,"securef/add.html")
        else:
            statement="Invalid Credentials"
            return render(request,"securef/admlogin.html",{"statement":statement})
    return render(request,"securef/admlogin.html",)

def emp(request):
    return render(request,"securef/emplogin.html")

def adm_entry(request):
    return render(request,"securef/add.html")

def adm_job(request):
    statement=""
    if request.method == "POST":
        empid_=request.POST.get("empid")
        loc_=request.POST.get("location")
        e0=list(Empid.objects.values_list("empid"))

        for i in range(0,len(e0)):
            if (e0[i][0]==empid_):
                    f=Empid(empid_)
                    geoloc.objects.create(empid=f,geotag=loc_)
                    # g1=geoloc(empid=f,geotag=loc_)
                    # g1.save()
                    statement="Record Added Successfully"
                    break
            else:
                statement="Invalid Employee ID"
    return render(request,"securef/add.html",{"statement":statement})


    

