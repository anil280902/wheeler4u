from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from App1.models import Category, Subcategory ,Booking,Admin_earnings
from User.models import user
from django.contrib import messages
from .models import *



# Create your views here.
def providersignin(request):
    if request.method == "POST":
        Username = request.POST['Username']
        Password = request.POST['Password']

        if authenticate(username=Username, password=Password):
            user = authenticate(username=Username, password=Password)
            login(request, user)
            return redirect('indexprovider')
        else:
            messages.error(request, 'Bad Credentials | Please Enter Right Data')
            return redirect('providersignin')

    return render(request, 'providersignin.html')

def providersignup(request):
    if request.method == "POST":
        Provider_name = request.POST['Provider_name']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Phone_no = request.POST['Phone_no']
        Business_name = request.POST['Business_name']
        GST_id = request.POST['GST_id']
        Business_address = request.POST['Business_address']

        if User.objects.filter(username=Provider_name):
            messages.error(request,'Username Already Exist !')
            return redirect('usersignup')

        if User.objects.filter(email=Email):
            messages.error(request,'Email Already Registered !')
            return redirect('usersignup')

        if provider.objects.filter(Phone_no=Phone_no):
            messages.error(request, 'PhoneNo Is Already Registered !')
            return redirect('usersignup')

        if provider.objects.filter(GST_id=GST_id):
            messages.error(request, 'GST No is Already Registered !')
            return redirect('usersignup')

        p = User.objects.create_user(username=Provider_name,email=Email,password=Password)
        p.save()

        pro_d = provider.objects.create(p=p,Provider_name=Provider_name,Email=Email,Password=Password,
                                        Phone_no=Phone_no,Business_name=Business_name,GST_id=GST_id,
                                        Business_address=Business_address)

        return redirect('providersignin')

    return render(request, 'providersignup.html')

def forgotpro(request):
    return render(request, 'forgotpro.html')

def indexprovider(request):
    global bl, pc
    u = user.objects.all()
    uc = len(u)
    print(uc)

    b = Booking.objects.all()

    p = provider.objects.all()
    pc = 0
    for i in p:
        pc = pc + i.Earnings
        pct = pc

    e = Admin_earnings.objects.get(id=1)
    te = e.A_earnings
    today_date = date.today()

    context = {
        'uc': uc,
        'bl': b,
        'b': b,
        'pc': pct,
        'td': today_date,
        'te' : te
    }

    return render(request, 'indexprovider.html',context)

def addvehicle_pro(request):
    user=request.user.id
    print(user)

    if request.method=='POST':
        Pro_id = request.POST.get('Provider_id')
        Pro_obj = provider.objects.get(pk=Pro_id)

        B = request.POST.get('Brand_name')
        B_obj = Category.objects.get(pk=B)

        M = request.POST.get('Vehicle_model')
        M_obj = Subcategory.objects.get(pk=M)

        Vehicle_number = request.POST['Vehicle_number']
        Chassis_no = request.POST['Chassis_no']
        Fuel_type = request.POST['Fuel_type']
        Transmission_type = request.POST['Transmission_type']
        Seating_capacity = request.POST['Seating_capacity']
        Rent_price = request.POST['Rent_price']
        Vehicle_img1 = request.POST['Vehicle_img1']
        Img_insurance = request.POST['Img_insurance']

        vid = Vehicle.objects.create(Provider_id = Pro_obj,
                                     Brand_name = B_obj,
                                     Vehicle_model = M_obj,
                                     Vehicle_number = Vehicle_number,
                                     Chassis_no = Chassis_no,
                                     Fuel_type=Fuel_type,
                                     Transmission_type = Transmission_type,
                                     Seating_capacity = Seating_capacity,
                                     Rent_price = Rent_price,
                                     Vehicle_img1 = Vehicle_img1,
                                     Img_insurance = Img_insurance)
    pid = provider.objects.all()
    cid = Category.objects.all()
    scid = Subcategory.objects.all()

    context = {
        'pid': pid,
        'cid': cid,
        'scid': scid
    }
    return render(request, 'addvehicle_pro.html',context)

def load_sub(request):
    country_id = request.GET.get('Category_id')
    # print(country_id,'country_id')
    s_id = request.GET.get('sub_id')
    # print(s_id, 's_id')
    subcat = Subcategory.objects.filter(Cat_name=country_id).order_by('Subcategory')
    # print(subcat)
    return render(request,'load_sub.html',{'subcat':subcat})

def vehiclelist(request):

    vid = Vehicle.objects.all()

    context = {
        'vid': vid
    }

    return render(request, 'vehiclelist.html',context)

def allbookings_pro(request):
    bid = Booking.objects.all()

    context = {
        'bid': bid,
    }
    return render(request, 'allbookings_pro.html',context)

def todaybookings_pro(request):
    today_date = date.today()
    bid = Booking.objects.all()
    context = {
        'bid': bid,
        'td': today_date
    }
    return render(request, 'todaybookings_pro.html',context)

def pwold(request):
    return render(request,'pwold.html')

def pwnew(request):
    return render(request,'pwnew.html')

def provider_profile(request):
    return render(request,'provider_profile.html')

def logout_pro1(request):
    logout(request)
    return redirect('providersignin')


