
#fisierul unde sunt definite paginile aplicatiei


###############################PAS 3 a codului####################### 

#Din urls.py se va veni aici si se vor apela aceste functii handlers pt diferite rute
#Aici sunt functiile ce se vor apela la diferite rute care sunt scrise in urls.py
#functie ce handles the traffic from the home page-ul blogului nostru


from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post   #din fisierul models.py luam clasa Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #LoginRequiredMixin pt ca atunci cand un utilizator nu e logat sa nu aiba acces la crearea unei postari
														#UserPassesTestMixin pt ca utilizatorii sa iti poate updata doar postarile facute de ei. Ei sa nu poate updata postari facute de alt user
#posts=[   #dummy data
#	{
#		'author': 'Anette dummy data',
#		'title': 'bloggy post 2 dumy data',
#		'content': 'contentull dummy data',
#		'date_posted':'august 15 1998'
#	},
#	{
#		'author': 'Ana dummy data',
#		'title': 'bloggy post 2 dummy data',
#		'content': 'contentul2 dummy data',
#		'date_posted':'august 11 2021'
#	}
#]


#functii ce fac render la template-urile noastre

def home(request):
	#return HttpResponse('<h1>Blog Home<h1>')      #acest response ne va transmite mesajul "Blog Home"

	context={
	#	'posts':posts   #pass dummy data
		'posts': Post.objects.all()
	}

	return render(request,'tweet_app/home.html',context)   #in localhost:8000/ (homepage-ul) punem cod html. Pentru a nu incarca mult codul si a fi inestetic, 
												   #cream template-uri unde ne scriem acest cod html

class PostListView(ListView):
	model = Post
	template_name= 'tweet_app/home.html'  #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'   #variabila pe care o sa lucram
	ordering = ['-date_posted']   #ordonam postarile. prima data va aparea cea mai nou postare, dupa cele vechi


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):  #LoginRequiredMixin ne va redirecta la pagina de login daca nu suntem logati si vrem sa facem o postare
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
    	form.instance.author=self.request.user  #punem autorul postarii ca find userul care face postarea
    	return super().form_valid(form)			


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
    	form.instance.author=self.request.user  
    	return super().form_valid(form)	

    def test_func(self):
    	post = self.get_object()
    	if self.request.user== post.author:  #daca userul care vrea sa modifice postarea este totodata autorul postarii, atunci poate updata postarea
    		return True
    	return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/'    #cand stergem o postare cu succes o sa fim redirectati la homepage

    def test_func(self):
    	post = self.get_object()
    	if self.request.user== post.author:  #daca userul care vrea sa modifice postarea este totodata autorul postarii, atunci poate updata postarea
    		return True
    	return False



def about(request):
	return render(request,'tweet_app/about.html',{'title':'About'})

def potiuni(request):
	return render(request,'tweet_app/potiuni.html',{'title':'potiuni'})
def cristale(request):
	return render(request,'tweet_app/cristale.html',{'title':'cristale'})
def manifestari(request):
	return render(request,'tweet_app/manifestari.html',{'title':'manifestari'})
def numerologie(request):
	return render(request,'tweet_app/numerologie.html',{'title':'numerologie'})
def ritualuri(request):
	return render(request,'tweet_app/ritualuri.html',{'title':'ritualuri'})
def incantatii(request):
	return render(request,'tweet_app/incantatii.html',{'title':'incantatii'})
def blesteme(request):
	return render(request,'tweet_app/blesteme.html',{'title':'blesteme'})




