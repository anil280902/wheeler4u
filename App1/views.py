from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from Provider.models import Vehicle,provider
from User.models import user
from django.contrib.auth import authenticate, login,logout
from datetime import datetime , date
from django.contrib import messages
from .models import *

# Create your views here.

def adminsignin(request):
    if request.method == "POST":
        Username = request.POST['Username']
        Password = request.POST['Password']

        if authenticate(username=Username,password=Password):
            su = authenticate(username=Username,password=Password).is_superuser
            if su == True:
                user = authenticate(username=Username,password=Password)
                login(request, user)
                return redirect('indexadmin')
        else:
            messages.error(request, 'Bad Credentials | Please Enter Right Data')
            return redirect('adminsignin')

    return render(request, 'adminsignin.html')

def forgotad(request):
    return render(request, 'forgotad.html')

def indexadmin(request):
    u = user.objects.all()
    uc = len(u)

    b = Booking.objects.all()
    bl = len(b)

    p = provider.objects.all()
    pc = len(p)

    e = Admin_earnings.objects.get(id=1)
    te = e.A_earnings

    today_date = date.today()

    context = {
        'uc' : uc,
        'bl' : bl,
        'b' : b,
        'pc' : pc,
        'te' : te,
        'td' : today_date
    }

    return render(request, 'indexadmin.html',context)

# def addvehicle_admin(request):
#     if request.method=='POST':
#         Provider_id = request.POST['Provider_id']
#         Brand_name = request.POST['Brand_name']
#         Vehicle_model = request.POST['Vehicle_model']
#         Vehicle_number = request.POST['Vehicle_number']
#         Chassis_no = request.POST['Chassis_no']
#         Fuel_type = request.POST['Fuel_type']
#         Transmission_type = request.POST['Transmission_type']
#         Seating_capacity = request.POST['Seating_capacity']
#         Rent_price = request.POST['Rent_price']
#         Vehicle_img1 = request.POST['Vehicle_img1']
#         Img_insurance = request.POST['Img_insurance']
#
#         vid = Vehicle.objects.create(Provider_id = Provider_id,
#                                      Brand_name = Brand_name,
#                                      Vehicle_model = Vehicle_model,
#                                      Vehicle_number = Vehicle_number,
#                                      Chassis_no = Chassis_no,
#                                      Fuel_type=Fuel_type,
#                                      Transmission_type = Transmission_type,
#                                      Seating_capacity = Seating_capacity,
#                                      Rent_price = Rent_price,
#                                      Vehicle_img1 = Vehicle_img1,
#                                      Img_insurance = Img_insurance)
#     cid = Category.objects.all()
#     scid = Subcategory.objects.all()
#
#     context = {
#         'cid': cid,
#         'scid': scid
#     }
#
#     return render(request, 'addvehicle_admin.html',context)


def vehiclelist_admin(request):
    spid = None
    if request.method == "POST":
        pname = request.POST['pname']
        print(pname)

        if pname != "All category" :
            spid = provider.objects.get(id=pname)
        else:
            spid = None

    vid = Vehicle.objects.all()
    pid = provider.objects.all()

    context = {
        'vid':vid,
        'pid':pid,
        'spid':spid
    }

    return render(request, 'vehiclelist_admin.html',context)

def addcat(request):
    if request.method == 'POST':
        Category_name = request.POST['Category_name']

        cid = Category.objects.create(Category_name=Category_name)

    return render(request,'addcat.html')

# def subcategory(request):
#     if request.method == 'POST':
#         Cat_name = request.POST['Category']
#         Subcategory = request.POST['Subcategory']
#
#         scid = Subcategory.objects.create(Subcategory=Subcategory,Cat_name=Cat_name)
#
#
#     cid = Category.objects.all()
#
#     context = {
#         'cid': cid
#     }
#
#     return render(request,'subcategory.html',context)
# def load_sub(request):
#     country_id = request.GET.get('Category_id')
#     print(country_id,'country_id')
#     s_id = request.GET.get('sub_id')
#     print(s_id, 's_id')
#     subcat = Subcategory.objects.filter(Cat_name=country_id).order_by('Subcategory')
#     print(subcat)
#     return render(request,'load_sub.html',{'subcat':subcat})


def subcategory(request):
    if request.method == 'POST':
        cat_id = request.POST.get('Category')  # Retrieve the selected category ID
        cat_obj = Category.objects.get(pk=cat_id)  # Get the Category object
        subcategory_name = request.POST['Subcategory']

        # Create the Subcategory object and associate it with the selected category
        subcategory = Subcategory.objects.create(Subcategory=subcategory_name, Cat_name=cat_obj)
        return redirect('subcategory')  # Redirect to the same page after adding the subcategory

    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'subcategory.html', context)

def showcat(request):
    cid = Category.objects.all()
    context = {
        'cid': cid
    }
    return render(request,'showcat.html',context)

def showsubcat(request):
    scid = Subcategory.objects.all()
    context = {
        'scid':scid
    }
    return render(request,'showsubcat.html',context)

def todaybookings(request):
    today_date = date.today()
    bid = Booking.objects.all()
    context = {
        'bid' : bid,
        'td' : today_date
    }
    return render(request, 'todaybookings.html',context)

def allbookings(request):
    bid = Booking.objects.all()
    context = {
        'bid' : bid,
    }
    return render(request, 'allbookings.html',context)

def changepw(request):
    return render(request,'changepw.html')

def changepw1(request):
    return render(request,'changepw1.html')

def admin_profile(request):
    return render(request,'admin_profile.html')

def logout1(request):
    logout(request)
    return redirect('adminsignin')