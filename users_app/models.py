


from django.db import models
from django.contrib.auth.models import User


#aici facem tabele ce vor aparea in django administration
# trebuie sa dam din cmd python manage.py makemigration ca sa fie luat acest cod si
# python manage.py migrate pt ca acest cod sa fie rulat

# one to one relationship. un utilizator poate avea doar un singur profil, iar un singur profil poate avea doar un utilizator
class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)   #CASCADE pt ca atunci cand se sterge un user, se va sterge si profilul
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):     #se cheama metoda dunder
		return f'{self.user.username} Profile'