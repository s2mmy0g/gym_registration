from django.shortcuts import render,redirect
from register.models import Register
from register.forms import RegisterForm
from authenticate import Authentication
# Create your views here.
@Authentication.valid_user
def index(request):
    print(request.method)
    if(request.method=="POST"):
        page=int(request.POST['page'])

        if('prev' in request.POST):
            page=page-1

        if('next' in request.POST):
            page=page+1

        tempOffSet=page-1
        offset=tempOffSet*4
        print(offset)

    else:
        offset=0
        page=1

    register=Register.objects.raw("select * from register limit 4 offset %s",[offset])
    pageItem=len(register)
    return render(request,"register/index.html",{'register':register,'page':page,'pageItem':pageItem})

@Authentication.valid_user
def search(request):
    print(request.POST['search'])
    register=Register.objects.get(register_id=request.POST['search'])
    return render(request,"register/search.html",{'register':register})

@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=RegisterForm(request.POST,request.FILES)
        form.save()
        return redirect("/register")
    else:
        form=RegisterForm()
    return render(request,"register/create.html",{'form':form})