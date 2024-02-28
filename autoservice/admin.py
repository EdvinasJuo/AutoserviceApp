from django.contrib import admin

# Register your models here.
from .models import Car, CarModel, Service, OrderLine, Profile

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'owner_name', 'license_plate', 'vin_number')


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'engine')
    list_filter = ('make', 'year')
    search_fields = ('make', 'model', 'year')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'price')

class OrderLinesAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 'order_date', 'car', 'quantity', 'repair_status', 'car_problem')
    search_fields = ('service__name', 'order__date', 'repair_status')
    filter_horizontal = ('services',)

admin.site.register(Profile)
admin.site.register(Car, CarAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OrderLine, OrderLinesAdmin)