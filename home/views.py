from django.shortcuts import render,redirect
from customer.models import Customer
from customer.forms import CustomerForm
    # Create your views here.
def index(request):
    customer=Customer.objects.all()
    return render(request,'home/index.html' ,{'customer':customer})


def register(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        result = form.save()
        request.session['customer_id'] = result.customer_id
        return redirect("/")
    else:
        form = CustomerForm()
    return render(request, "home/register.html", {'form': form})


def login(request):
    if (request.method == 'POST'):
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']

        return redirect("/user")

    return render(request, "home/login.html")


def logout(request):
    request.session.clear()
    return redirect("/")

def s404(request):
    customer = Customer.objects.all()
    return render(request, 'home/404.html', {'customer': customer})

def about_us(request):
    customer = Customer.objects.all()
    return render(request, 'home/about-us.html', {'customer': customer})


def blog(request):
    customer = Customer.objects.all()
    return render(request, 'home/blog.html', {'customer': customer})

def blog_details(request):
    customer = Customer.objects.all()
    return render(request, 'home/blog-details.html', {'customer': customer})


def bmi_calculator(request):
    customer = Customer.objects.all()
    return render(request, 'home/bmi-calculator.html', {'customer': customer})


def class_details(request):
    customer = Customer.objects.all()
    return render(request, 'home/class-details.html', {'customer': customer})


def class_timetable(request):
    customer = Customer.objects.all()
    return render(request, 'home/class-timetable.html', {'customer': customer})


def contact(request):
    customer = Customer.objects.all()
    return render(request, 'home/contact.html', {'customer': customer})


def gallery(request):
    customer = Customer.objects.all()
    return render(request, 'home/gallery.html', {'customer': customer})


def services(request):
    customer = Customer.objects.all()
    return render(request, 'home/services.html', {'customer': customer})


def team(request):
    customer = Customer.objects.all()
    return render(request, 'home/team.html', {'customer': customer})



