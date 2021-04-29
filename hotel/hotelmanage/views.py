
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from numpy import random
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response

from .forms import CustomerRegistrationForm
from .models import customer_reg_form, generate_bill, room_booking_form
from  rest_framework.decorators import api_view

from datetime import datetime, date

from .serializers import EmployeeSerializers


def sign_up(request):
    if request.method == 'POST':
        print("Nisar")
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            print("bix")
            form.save()
            return render(request, 'home_page.html', {})
    form = UserCreationForm
    return render(request, 'Sign_up.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        us = authenticate(request, username=u, password=p)
        if us is not None:
            login(request, us)
            print('sssss')
            return redirect('/cust_dashboard/')
    return render(request, 'home_page.html', {})

@login_required(login_url='/login_page/')
def cust_dashboard(request):
    if request.method == "POST":
        if request.POST.get('login'):
            return HttpResponseRedirect('/customer_login')
        if request.POST.get('register'):
            return HttpResponseRedirect('/cust_registration_html')
        if request.POST.get('logout'):
            return HttpResponseRedirect('/home_page')
    return render(request, 'cust_dashboard.html', {})


# def cust_registration(request):
#     if request.method == "POST":
#         form = CustomerRegistrationForm(request.POST)
#         print(form)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/customer_login/')
#         else:
#             return HttpResponse('/invalid')
#     form = CustomerRegistrationForm
#     return render(request, 'cust_registration_page.html', {'form': form})
@login_required(login_url='/login_page/')
def cust_registration_html(request):
    if request.method == "POST":
        cname = request.POST['your name']
        caddress = request.POST['your address']
        cmail_id = request.POST['your mail id']
        cmobile_no = request.POST['your mobile number']
        cusername = request.POST['your username']
        cpassword = request.POST['your password']
        customer_reg_form.objects.create(c_name=cname, c_address=caddress, c_mail_id=cmail_id,
                                         c_mob_no=cmobile_no, c_username=cusername, c_password=cpassword)
        return HttpResponseRedirect('/customer_login/')
    return render(request, 'cust_registration_page.html', {})

@login_required(login_url='/login_page/')
def customer_login(request):
    if request.method == "POST":
        cusername = request.POST.get('your username')
        cpassword = request.POST.get('your password')
        record = customer_reg_form.objects.filter(c_username=cusername, c_password=cpassword)
        if record:
            return HttpResponseRedirect('/cust_home_page')
        if request.POST.get('goto home'):
            return HttpResponseRedirect('/home_page')
        else:
            return HttpResponseRedirect('/invalid')
    return render(request, 'cust_login_page.html', {})

@login_required(login_url='/login_page/')
def invalid(request):
    return HttpResponse("Invalid username or password")

@login_required(login_url='/login_page/')
def cust_home_page(request):
    if request.method == "POST":
        if request.POST.get("book_room"):
            return HttpResponseRedirect('/cust_room_booking')
        if request.POST.get("details"):
            return HttpResponseRedirect('/sample')
        if request.POST.get("bill"):
            return HttpResponseRedirect('/generate_bill_code')
        if request.POST.get("logout"):
            return HttpResponseRedirect('/home_page')
    return render(request, 'cust_home_page.html', {})

@login_required(login_url='/login_page/')
def cust_room_booking(request):
    global room_num
    room_num = random.randint(100, 999)
    if request.method == "POST":
        name = request.POST.get('cust_name')
        num_of_ad = request.POST['no_of_adults']
        x = int(num_of_ad)
        name_of_ad = request.POST['name_of_adults']
        num_of_ch = request.POST['no_of_child']
        y = int(num_of_ch)
        name_of_child = request.POST['name_of_child']
        phone_num = request.POST['phone']
        check_in_date_time = request.POST['check_in']
        check_out_date_time = request.POST['check_out']
        total = (x * 100 + y * 50)
        room_num1=0
        if x==3 or y==3 or (x+y)>3:
            room_num1=random.randint(100,999)
        room_booking_form.objects.create(name=name, no_adults=num_of_ad, name_adults=name_of_ad, no_child=num_of_ch,
                                         name_child=name_of_child, phone_num=phone_num,
                                         check_in_date=check_in_date_time, check_out_date=check_out_date_time,
                                         room_no=room_num,room_no1=room_num1)
        generate_bill.objects.create(room_no=room_num, b_name=name, mob_num=phone_num,
                                     check_in=check_in_date_time, check_out=check_out_date_time,
                                     total=total)
        record = {'roomalloc': room_booking_form.objects.all().filter(name=name)}
        return render(request, 'after_room_booking.html', record)

    return render(request, 'room_booking.html', {})

@login_required(login_url='/login_page/')
def sample(request):
    if request.method == "POST":
        rno = request.POST.get('room_no')
        print(rno)
        record = {'details': room_booking_form.objects.all().filter(room_no=rno)}
        print(record)
        if request.POST.get('bill'):
            return render(request, 'sample_view.html', record)
    return render(request, 'sample.html', {})

@login_required(login_url='/login_page/')
def after_booking(request):
    if request.method == "POST":
        tname = request.POST.get('cust_name')
        record = {'roomalloc': room_booking_form.objects.all().filter(name=tname)}
        if request.POST.get('back'):
            return HttpResponseRedirect('/cust_home_page')
        return render(request, 'after_room_booking.html', record)

    return render(request, 'room_booking.html', {})

@login_required(login_url='/login_page/')
def generate_bill_code(request):
    if request.method == "POST":
        rno = request.POST.get('room_no')
        print(rno)
        record = {'billing': generate_bill.objects.all().filter(room_no=rno)}
        print(record)
        return render(request, 'bill_page.html', record)
    else:
        print("my mistake")
    return render(request, 'gen_bill.html', {})

@login_required(login_url='/login_page/')
def logout_page(request):
    logout(request)
    return redirect('/login_page/')


@api_view(['POST'])
def mysign_up(request):

    if request.method == 'POST':
        serialize_data = EmployeeSerializers(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        return Response({'Error': 'BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)