from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from faker import Faker

from . import forms
from . import models
import random


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return HttpResponseRedirect("/admin")
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        return render(request, "sihapp/home.html", {})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def login_user(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        user = authenticate(username=uname, password=pwd)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("User not found!")
    else:
        return HttpResponseRedirect(reverse('home'))


def random_forest(sales):
    pass


def suggest(request):
    if request.user.is_authenticated:
        showroom = models.ShowRoom.objects.get(user=request.user)
        sales = showroom.sales.all()
        data = {}
        types = ['newspaper', 'tvads', 'exchangeoffers', 'melas', 'other']
        grps = []
        frequency = sales.count()
        for type in types:
            val = sales.filter(mode_known__exact=type).count()
            grps.append((val / frequency) * 100)
        ind = grps.index(max(grps))
        best_action = random_forest(sales)
        best_action = types[ind]
        return render(request, "sihapp/suggest.html", {'best_action': best_action})


def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            showroom = models.ShowRoom.objects.get(user=request.user)
            scooters = showroom.sales.filter(vehicle_type="scooters")
            motorcycles = showroom.sales.filter(vehicle_type="motorcycles")
            mopeds = showroom.sales.filter(vehicle_type="moped")
            three_wheelers = showroom.sales.filter(vehicle_type="three_wheelers")
            return render(request, "sihapp/dashboard.html",
                          {'scooters': scooters, 'motorcycles': motorcycles, 'mopeds': mopeds,
                           'three_wheelers': three_wheelers})
        elif request.user.is_superuser:
            return HttpResponseRedirect("/admin")
    else:
        return HttpResponseRedirect(reverse('home'))


def sale(request):
    form = forms.SaleForm
    if request.method == 'POST':
        form = forms.SaleForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse(form.errors)

    return render(request, "sihapp/sale.html", {'form': form})


def populate(request):
    d = {
        'scooters': ['ntorq', 'jupiter', 'wego', 'zest', 'pep+'],
        'motorcycles': ['victor', 'sport', 'radeon', 'star city+', 'apache rtr 160 4v', 'apache rtr 200 4v',
                        'apache rr310'],
        'moped': ['xl100', ],
        'three_wheelers': ['king', ]
    }
    for i in range(100):
        fake = Faker()
        fake_name = fake.name()
        fake_mobile = random.randint(9000000001, 9999999999)
        fake_location = random.choice(['guntur', 'vijayawada', 'coimbatore'])
        fake_location_type = random.choice(['rural', 'urban'])
        fake_age = random.randint(18, 60)
        fake_gender = random.choice(['male', 'female'])
        fake_vehicle_type = random.choice(list(d.keys()))
        fake_vehicle_name = random.choice(d[fake_vehicle_type])
        fake_color = random.choice(['red', 'green', 'blue', 'silver', 'black'])
        fake_mode = random.choice(['newspaper', 'tvads', 'exchangeoffers', 'melas', 'other'])
        showroom = models.ShowRoom.objects.get(user=request.user)
        obj = models.Sale.objects.create(name=fake_name, mobile_number=fake_mobile, location=fake_location,
                                         location_type=fake_location_type,
                                         age=fake_age, gender=fake_gender, vehicle_type=fake_vehicle_type,
                                         vehicle_name=fake_vehicle_name,
                                         vehicle_color=fake_color, mode_known=fake_mode)
        showroom.sales.add(obj)
    return HttpResponseRedirect(reverse('home'))


def ajax_grp_whole(request):
    if request.user.is_authenticated:
        showroom = models.ShowRoom.objects.get(user=request.user)
        sales = showroom.sales.all()
        data = {}
        types = ['newspaper', 'tvads', 'exchangeoffers', 'melas', 'other']
        grps = []
        frequency = sales.count()
        for type in types:
            val = sales.filter(mode_known__exact=type).count()
            grps.append((val / frequency) * 100)
        data['labels'] = types
        data['data'] = grps
        return JsonResponse(data)


def ajax_grp_type(request, type):
    if request.user.is_authenticated:
        print(type)
        if type == "all":
            ajax_grp_whole(request)
        showroom = models.ShowRoom.objects.get(user=request.user)
        sales = showroom.sales.filter(vehicle_type=type)
        data = {}
        types = ['newspaper', 'tvads', 'exchangeoffers', 'melas', 'other']
        grps = []
        frequency = sales.count()
        for type in types:
            val = sales.filter(mode_known__exact=type).count()
            grps.append((val / frequency) * 100)
        data['labels'] = types
        data['data'] = grps
        return JsonResponse(data)
