
#fisier unde sunt definite modelele(tabelele) folosite in aplicatie
#aici facem tabele ce vor aparea in django administration
# trebuie sa dam din cmd python manage.py makemigration ca sa fie luat acest cod si
# python manage.py migrate pt ca acest cod sa fie rulat





from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #importam user model. intre user si post o sa fie o relatie one-to-many
from django.urls import reverse

class Post(models.Model):
	title= models.CharField(max_length=100)
	content=models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)	#foreign key pt ca sa fie doar un singur autor utilizator ce poate avea mai multe postari
																#pune on_delete pt ca in cazul in care un user e sters, si postarile sale vor fi sterse


	def __str__(self):
		return self.title    #cand scriem in shell comanda Post.objects.all(), ne va afisa queryul cu titlul postului   <QuerySet [<Post: TitluBlog1>]>
							#fara aceasta functie se afisa un query fara titluri obiectelor si astfel este mai greu de identificat fiecare post
							# <QuerySet [<Post: Post object (1)>]>

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})    #dupa ce cream o postare o sa fim trimisi pe ruta postarii 
																# de la http://localhost:8000/post/new/ catre http://localhost:8000/post/7/
																													



#folosim reverse function -> return the full url to that route as a string
#nu utilizam redirect function ->redirects you to a specific route