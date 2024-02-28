from django.db.models.signals import post_save  # signalas
from django.contrib.auth.models import User     # siuntejas
from django.dispatch import receiver            # priėmejas (dekoratorius)
from .models import Profile

# sukurus vartotoja automatiskai sukuriamas ir profile
@receiver(post_save, sender=User) # jeigu išsaugojamas User objektas, inicijuojama f-ja po dekoratoriumi
def create_profile(sender, instance, created, **kwargs): # instance yra ką tik sukurtas User objektas.
    if created:
        Profile.objects.create(user=instance)
        print('KWARGS: ', kwargs)


# Pakoregavus vartotoją, išsaugomas ir profilis
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()