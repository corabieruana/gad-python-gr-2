
# Signals allow certain senders to notify a set of receivers that some action has taken place. They’re especially useful when many pieces of code may be interested in the same events.
#semnalele pornesc functiile ori de cate ori apar 

from django.db.models.signals import post_save   #semnal ce este produs cand un obiect e salvat
                                                    #vom obtine un post_save signal cand un utilizator este creat
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#dorim ca un user profile sa fie creat pt fiecare utilziator



@receiver(post_save, sender=User)  # receiver primeste semnalul (post_save=semnalul transmis cand este creat un user, 
                                    #sender_User=crearea userului ce va trimite semnalul post_save)    
                                    #receiver-ul este, de fapt, functia create_profile
def create_profile(sender, instance, created, **kwargs):       #functie ce creaza profilul unui utilizator. aceasta fct va fi rulata de fiecare data cand un utilziator e creat
    if created:
        Profile.objects.create(user=instance) #creaza un profil pt utilizatorul ce a fost creat



@receiver(post_save, sender=User)         #functie ce salveaza profilul de fiecare data cand userul e salvat
def save_profile(sender, instance, **kwargs):
    instance.profile.save()