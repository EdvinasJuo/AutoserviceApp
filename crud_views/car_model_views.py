from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from autoservice.models import CarModel

class CarModelDetailView(LoginRequiredMixin, generic.DetailView):
    model = CarModel
    template_name = 'Car_model/car_model.html'
    context_object_name = 'car_model'
    pk_url_kwarg = 'car_model_id'

class CarModelCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = CarModel
    fields = ['make', 'model', 'year' ,'engine']
    success_url = reverse_lazy('car_models') # sugeneruoja URL dinaminiu budu
    template_name = 'Car_model/car_model_form.html'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class CarModelUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = CarModel
    fields = ['make', 'model', 'year' ,'engine']
    success_url = reverse_lazy('car_models')
    template_name = 'Car_model/car_model_form.html'
    pk_url_kwarg = 'car_model_id'

    def test_func(self):
        return self.request.user.is_superuser #Jeigu super admin leis update, jeigu ne numes i 403 forbidden

class CarModelDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = CarModel
    success_url = reverse_lazy('car_models')  # sugeneruoja URL dinaminiu budu
    template_name = 'Car_model/car_model_delete.html'
    pk_url_kwarg = 'car_model_id'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_model'] = self.get_object()  # paduodi car_model objekta i context
        return context