from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} - {self.price} EUR"

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class CarModel(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    engine = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.engine})"

    class Meta:
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"

class Car(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    vin_number = models.CharField(max_length=17)
    cover = models.ImageField('Cover', upload_to='covers', null=True)

    def __str__(self):
        return f"{self.car_model} - {self.owner_name} ({self.license_plate})"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

class OrderLine(models.Model):
    services = models.ManyToManyField(Service)
    order_date = models.DateField(default=timezone.now, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=None, null=True)
    quantity = models.PositiveIntegerField()
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    REPAIR_STATUS = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    repair_status = models.CharField(max_length=20, choices=REPAIR_STATUS, default='Pending')
    car_problem = models.CharField(max_length=500, default='Problem comment')

    @property
    def total_cost(self):
        return sum(service.price for service in self.services.all()) * self.quantity

    def __str__(self):
        return f'OrderLine = {", ".join(str(service) for service in self.services.all())}, {self.order_date}, {self.quantity}, {self.repair_status}, {self.car_problem}'

    class Meta:
        verbose_name = "Order Line"
        verbose_name_plural = "Order Lines"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profile"