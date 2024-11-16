from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


from visits.models import PageVisits
this_dir=pathlib.Path(__file__).resolve().parent

def home_view(request,*args,**kwargs):
   return about_view(request,*args,**kwargs)



def about_view(request,*args,**kwargs):
    """"
    html_=""
    location=this_dir / "home.html"
    html_=location.read_text()
    """
    query_set=PageVisits.objects.all()
    page_qs=PageVisits.objects.filter(path=request.path)
    try:
        percent=(page_qs.count()*100)/query_set.count()
    except:
        percent=0
    count_visits=query_set.count()
    html_template="home.html"
    mon_titre="First Saas"
    my_context={
        "page_title":mon_titre,
        "visits":query_set,
        "count_visits":count_visits,
        "page_visits":page_qs.count(),
        "percent":percent
    }
    PageVisits.objects.create(path=request.path)
    return render(request,html_template,my_context)


VALID_CODE="abc123"

def pw_protected_view(request,*args,**kwargs):
    is_allowed=request.session.get("protected_page_allowed") or 0
    print(request.session.get("protected_page_allowed"), type(request.session.get("protected_page_allowed") ))
    if request.method=="POST":
        user_pw = request.session.get("protected_page_allowed")
        if user_pw ==VALID_CODE:
             request.session["protected_page_allowed"]
    if is_allowed:
        return render(request,"protected/view.html")
    return render(request,"protected/entry.html")