from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Car, CarModel, Service, OrderLine


# Create your views here.

def index(request):
    # suskaiciuojami service ir orders objektai
    num_services = Service.objects.all().count()
    num_cars = CarModel.objects.all().count()

    total_orders = OrderLine.objects.all().count()

    # suskaiciuojami in progress uzsakymai.
    num_orders_in_progress = OrderLine.objects.filter(repair_status__exact='In Progress').count()

    # suskaiciuojami in progress uzsakymai.
    num_orders_pending = OrderLine.objects.filter(repair_status__exact='Pending').count()

    num_orders_completed = OrderLine.objects.filter(repair_status__exact='Completed').count()

    num_customers = Car.objects.all().count()

    context = {
        'num_services': num_services,
        'num_orders_in_progress': num_orders_in_progress,
        'num_cars': num_cars,
        'num_orders_pending': num_orders_pending,
        'num_orders_completed': num_orders_completed,
        'total_orders': total_orders,
        'num_customers': num_customers,
    }
    return render(request, 'index.html', context=context)


def car_models(request):
    car_models = CarModel.objects.all()

    query = request.GET.get('q')
    if query:
        search_car_model = CarModel.objects.filter(
            Q(make__icontains=query) |
            Q(model__icontains=query) |
            Q(year__icontains=query) |
            Q(engine__icontains=query)
        )
        car_models = search_car_model

    # Puslapiavimas
    page = request.GET.get('page', 1)
    paginator = Paginator(car_models, 5)

    try:
        car_models = paginator.page(page)
    except PageNotAnInteger:
        car_models = paginator.page(1)
    except EmptyPage:
        car_models = paginator.page(paginator.num_pages)

    context = {
        'car_models': car_models
    }
    return render(request, 'Car_model/car_models.html', context=context)


def unauthorized_access(request):
    messages.error(request, 'You do not have permission to access this page.')
    return redirect('login')


@user_passes_test(lambda u: u.is_superuser, login_url='unauthorized_access')
def customers(request):
    customers = Car.objects.all()

    # Paieskos laukelis
    query = request.GET.get('q')
    if query:
        search_customers = Car.objects.filter(
            Q(car_model__make__icontains=query) |
            Q(car_model__model__icontains=query) |
            Q(owner_name__icontains=query) |
            Q(license_plate__icontains=query) |
            Q(vin_number__icontains=query)
        )
        customers = search_customers

    # Puslapiavimas
    page = request.GET.get('page', 1)
    paginator = Paginator(customers, 5)

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    context = {
        'customers': customers
    }
    return render(request, 'Customers/customers.html', context=context)


def services(request):
    services = Service.objects.all()

    query = request.GET.get('q')
    if query:
        search_services = Service.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query)
        )
        services = search_services

    # Puslapiavimas
    page = request.GET.get('page', 1)
    paginator = Paginator(services, 5)

    try:
        services = paginator.page(page)
    except PageNotAnInteger:
        services = paginator.page(1)
    except EmptyPage:
        services = paginator.page(paginator.num_pages)

    context = {
        'services': services
    }
    return render(request, 'Services/services.html', context=context)


@user_passes_test(lambda u: u.is_superuser, login_url='unauthorized_access')
def order_lines(request):
    order_lines = OrderLine.objects.all()

    # Paieskos laukelis
    query = request.GET.get('q')
    if query:
        search_orders = OrderLine.objects.filter(
            Q(car__car_model__make__icontains=query) |
            Q(car__car_model__model__icontains=query) |
            Q(car__car_model__year__icontains=query) |
            Q(car__license_plate__icontains=query) |
            Q(order_date__icontains=query) |
            Q(repair_status__icontains=query) |
            Q(car_problem__icontains=query)
        )
        order_lines = search_orders

    # Puslapiavimas
    page = request.GET.get('page', 1)
    paginator = Paginator(order_lines, 5)

    try:
        order_lines = paginator.page(page)
    except PageNotAnInteger:
        order_lines = paginator.page(1)
    except EmptyPage:
        order_lines = paginator.page(paginator.num_pages)

    context = {
        'order_lines': order_lines
    }
    return render(request, 'Order_lines/order_lines.html', context=context)


# ATVAIZDUOAMI TAM TIKRO USER UZSAKYMAI


class CarServicesByCustomer(LoginRequiredMixin, generic.ListView):
    model = OrderLine
    template_name = 'user_services.html'
    context_object_name = 'order_history'

    def get_queryset(self):
        # Filter OrderLines related to the currently logged-in user
        return OrderLine.objects.filter(customer=self.request.user)


@csrf_protect
def register(request):
    if request.method == "POST":
        # Gauti reiksmes is formos
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Patkrinti ar sutampa slaptazodziai
        if password == password2:
            # patikrinti ar toks username nera uzimtas
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} already exists!')
                return redirect('register')
            else:
                # patikrinti ar toks gmail nera uzimtas
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with email: {email} already exists!')
                    return redirect('register')
                else:
                    # sukurti nauju user kuriant uzsakova
                    customer = User.objects.create_user(username=username, email=email, password=password)

                    messages.success(request, f'Username {username} successfully registered!')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

    return render(request, 'registration/register.html')


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated succesfully")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)
