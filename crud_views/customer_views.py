from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from autoservice.models import Car, OrderLine


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car
    template_name = 'Customers/customer.html'
    context_object_name = 'customer'
    pk_url_kwarg = 'customer_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch the order history for the customer
        order_history = OrderLine.objects.filter(car=context['customer']).order_by('-order_date')

        context['order_history'] = order_history
        return context

class CustomerCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Car
    fields = ['car_model', 'owner_name', 'license_plate', 'vin_number', 'cover']
    success_url = reverse_lazy('customers')  # sugeneruoja URL dinaminiu budu
    template_name = 'Customers/customer_form.html'

    def form_valid(self, form):
        # sukuriamas naujas useris su username ir default passwordu
        user = User.objects.create_user(username=form.cleaned_data['owner_name'], password='Test123.')

        #priskiriamas useris 'car' instance
        form.instance.reader = user

        #issaugojamas ir sukuriamas 'car' instance
        response = super().form_valid(form)

        return response

    def test_func(self):
        return self.request.user.is_superuser

class CustomerUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Car
    fields = ['car_model', 'owner_name', 'license_plate', 'vin_number', 'cover']
    success_url = reverse_lazy('customers')
    template_name = 'Customers/customer_form.html'
    pk_url_kwarg = 'customer_id'

    def test_func(self):
        return self.request.user.is_superuser #Jeigu super admin leis update, jeigu ne numes i 403 forbidden

class CustomerDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Car
    success_url = reverse_lazy('customers')  # sugeneruoja URL dinaminiu budu
    template_name = 'Customers/customer_delete.html'
    pk_url_kwarg = 'customer_id'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = self.get_object()  # paduodi car_model objekta i context
        return context