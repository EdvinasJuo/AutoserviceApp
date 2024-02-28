from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from autoservice.models import OrderLine


class OrderLineDetailView(LoginRequiredMixin, generic.DetailView):
    model = OrderLine
    template_name = 'Order_lines/order_line.html'
    context_object_name = 'order_line'
    pk_url_kwarg = 'order_line_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_cost = context['order_line'].total_cost
        context['total_cost'] = total_cost

        return context


class OrderLineCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = OrderLine
    fields = ['services', 'order_date', 'car', 'quantity', 'customer', 'repair_status', 'car_problem']
    success_url = reverse_lazy('order_lines')  # sugeneruoja URL dinaminiu budu
    template_name = 'Order_lines/order_line_form.html'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class OrderLineUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = OrderLine
    fields = ['services', 'order_date', 'car', 'quantity', 'customer', 'repair_status', 'car_problem']
    success_url = reverse_lazy('order_lines')  # sugeneruoja URL dinaminiu budu
    template_name = 'Order_lines/order_line_form.html'
    pk_url_kwarg = 'order_line_id'

    def test_func(self):
        return self.request.user.is_superuser  # Jeigu super admin leis update, jeigu ne numes i 403 forbidden


class OrderLineDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = OrderLine
    success_url = reverse_lazy('order_lines')  # sugeneruoja URL dinaminiu budu
    template_name = 'Order_lines/order_line_delete.html'
    pk_url_kwarg = 'order_line_id'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_line'] = self.get_object()
        return context
