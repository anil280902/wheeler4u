from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from Provider.models import provider,Vehicle,Payment_provider
from App1.models import Booking,Payment,Admin_earnings
import razorpay
import uuid
from datetime import datetime

from django.contrib import messages

from .models import *
from Wheeler4U.settings import REZORPAY_API_KEY, RAZORPAY_API_SECRETKEY

# from Wheeler4U import settings


# Create your views here.

def usersignin(request):
    if request.method == "POST":
        username = request.POST['username']
        Password = request.POST['Password']

        if authenticate(username=username, password=Password):
            user = authenticate(username=username, password=Password)
            login(request, user)
            return redirect('indexuser')
        else:
            messages.error(request, 'Bad Credentials | Please Enter Right Data')
            return redirect('usersignin')


    return render(request, 'usersignin.html',)

def usersignup(request):
    if request.method == "POST":
        User_name = request.POST['User_name']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Gender = request.POST['Gender']
        Phone_no = request.POST['Phone_no']
        Licence_no = request.POST['Licence_no']
        Address = request.POST['Address']
        Deposit = 0

        if User.objects.filter(username=User_name):
            messages.error(request,'Username Already Exist !')
            return redirect('usersignup')

        if User.objects.filter(email=Email):
            messages.error(request,'Email Already Registered !')
            return redirect('usersignup')

        if user.objects.filter(Phone_no=Phone_no):
            messages.error(request, 'PhoneNo Is Already Registered !')
            return redirect('usersignup')

        if user.objects.filter(Licence_no=Licence_no):
            messages.error(request, 'LicenceNo is Already Registered !')
            return redirect('usersignup')


        u=User.objects.create_user(username=User_name,email=Email,password=Password)
        u.save()

        user_d = user.objects.create(u=u,User_name=User_name,Email=Email,Password=Password,
                                    Gender=Gender,Phone_no=Phone_no,Licence_no=Licence_no,
                                    Address=Address,Deposit=Deposit)

        return redirect('usersignin')

    return render(request,'usersignup.html')

@login_required
def indexuser(request):
    return render(request,'indexuser.html')


def cars(request):
    vid = Vehicle.objects.all()
    context = {
        'vid' : vid
    }
    return render(request,'cars.html',context)

def car_details(request,id):

    cid = Vehicle.objects.get(id=id)

    context = {
        'cid':cid
    }

    return render(request,'car_details.html',context)

@login_required
def payment(request):
    # u_name = request.user.id
    # ui = user.objects.get(pk=u_name)
    # print(ui)
    global p_earnings
    uid = user.objects.all()
    for i in uid:
        if i.User_name == request.user.username:
            ui = i.id
            u = user.objects.get(id=ui)
            o_deposit = u.Deposit
            # print(o_deposit)

            if o_deposit < 2000 :
                n_deposit = 2000 - o_deposit
                print(n_deposit)
            else:
                n_deposit = 0
                print("You Have Enough Deposit")

    vid = request.session.get('Vehicleid')
    vehicle_id = Vehicle.objects.get(id=vid)

    rent = vehicle_id.Rent_price
    print(rent)
    Provider_id = vehicle_id.Provider_id

    D = request.session.get('Duration')
    print(D)

    if o_deposit < 2000:
        total = n_deposit + rent * int(D)
        print(total)
    else:
        total = rent * int(D)

    r_total = total * 100

    # print(uid)
    # print(vehicle_id)
    # print(total)
    # print(datetime.now())
    # Invoice_no = uuid.uuid4().hex[:6]
    # print(Invoice_no)

    if r_total:
        client = razorpay.Client(auth=(REZORPAY_API_KEY, RAZORPAY_API_SECRETKEY))
        response = client.order.create({'amount': total, 'currency': 'INR', 'payment_capture': 1})
        print(response, "****************************************")

        Pay_date_time = datetime.now()
        Invoice_no = uuid.uuid4().hex[:12]

        pid = Payment.objects.create(User_id=u,Vehicle_id=vehicle_id,Amount=total,
                                     Pay_date_time=Pay_date_time,Invoice_no=Invoice_no)

        # Commission Calculation

        if o_deposit < 2000:
            a_earn = total - 2000
            a_earnings = a_earn / 10
            print('Admin E',a_earnings)
            p_earnings = a_earn - a_earnings
            print('Provider E',p_earnings)
        else:
            a_earn = total
            a_earnings = a_earn / 10
            print('Admin E', a_earnings)
            p_earnings = a_earn - a_earnings
            print('Provider E', p_earnings)


        p_pid = Payment_provider.objects.create(Provider_id=Provider_id,Vehicle_id=vehicle_id,Amount=p_earnings,
                                                Admin_commission=a_earnings,Pay_date_time=Pay_date_time,Invoice_no=Invoice_no)

        if pid:
            u.Deposit = 2000
            u.save()

        if p_pid:
            pvm = vehicle_id.Provider_id.id
            pvmp = provider.objects.get(id=pvm)
            pvmp.Earnings = pvmp.Earnings + p_earnings
            pvmp.save()

            ae = Admin_earnings.objects.get(id=1)
            ae.A_earnings = ae.A_earnings + a_earnings
            ae.save()

        B_start_date = request.session.get('B_start_date')
        B_end_date = request.session.get('B_end_date')
        Starting_location = request.session.get('Starting_location')
        Ending_location = request.session.get('Ending_location')

        Created_at = datetime.now()

        bid = Booking.objects.create(User_id=u, Provider_id=Provider_id, Vehicle_id=vehicle_id,
                                     B_start_date=B_start_date, B_end_date=B_end_date,Created_at=Created_at,
                                     Starting_location=Starting_location,Ending_location=Ending_location)


    context = {
        'o_deposit' : o_deposit,
        'n_deposit' : n_deposit,
        'rent' : rent,
        'D' : D,
        'total' : total,
        'r_total' : r_total
    }


    return render(request,'payment.html',context)

@login_required
def booking_info(request,id):

    # u1 = request.session.get('id')
    # print(u1)

    vid = Vehicle.objects.get(id=id)
    Provider_id = vid.Provider_id
    Vehicle_id = vid
    Vehicleid = vid.id
    request.session['Vehicleid'] = Vehicleid

    print(Provider_id)
    print(vid)

    vp = vid.Rent_price
    v_price = vp * 100
    # print(v_price)

    if request.method == "POST":

        # Provider_id = request.POST['Provider_id']
        # Vehicle_id = request.POST['Vehicle_id']
        B_start_date = request.POST.get('B_start_date')
        B_end_date = request.POST.get('B_end_date')
        Starting_location = request.POST.get('Starting_location')
        Ending_location = request.POST.get('Ending_location')

        date_format = '%Y-%m-%dT%H:%M'
        date1 = datetime.strptime(B_start_date, date_format)
        date2 = datetime.strptime(B_end_date, date_format)

        d = date2 - date1
        print(d.days)
        Duration = d.days + 1
        print(Duration)


        request.session['B_start_date'] = B_start_date
        request.session['B_end_date'] = B_end_date
        request.session['Starting_location'] = Starting_location
        request.session['Ending_location'] = Ending_location
        request.session['Duration'] = Duration

        return redirect('/user/payment/')

    ui = user.objects.all()

    context = {
        'v_price': v_price,
        'ui' : ui,
        'vid' : vid
    }

    return render(request,'booking_info.html',context)

@login_required
def profile(request):
    pid = user.objects.all()
    # for i in uid:
    #     if i.User_name == request.user.username:
    #         ui = i.id
    #         pid = user.objects.get(id=ui)
    #
    context = {
        'pid' : pid
    }

    return render(request,'profile.html',context)

def logout_u(request):
    logout(request)
    return redirect('usersignin')