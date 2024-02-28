from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from autoservice.models import Service

class ServiceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Service
    context_object_name = 'service'
    pk_url_kwarg = 'service_id'


class ServiceCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Service
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('services') # sugeneruoja URL dinaminiu budu
    template_name = 'Services/service_form.html'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Service
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('services')  # sugeneruoja URL dinaminiu budu
    template_name = 'Services/service_form.html'
    pk_url_kwarg = 'service_id'

    def test_func(self):
        return self.request.user.is_superuser #Jeigu super admin leis update, jeigu ne numes i 403 forbidden

class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Service
    success_url = reverse_lazy('services')  # sugeneruoja URL dinaminiu budu
    template_name = 'Services/service_delete.html'
    pk_url_kwarg = 'service_id'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.get_object()  # paduodi car_model objekta i context
        return context