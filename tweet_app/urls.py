

###############################PAS 2 a codului####################### 


#din urls.py a main project-ului(Tweeter_project) suntem trimisi aici


from django.urls import path
from . import views   #importam codul din views.py  Punctul inseamna ca suntem in directorul curent
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
   path('', PostListView.as_view(), name='tweet_app-home'),  #PostListView.as_view() se va uita in <app>/<model>_<viewtype>.html  adica dupa tweet_app/post_list.html
 #   path('', views.home, name='tweet_app-home'),  #ruta '', adica localhost:8000/ (homepage-ul). Cand ne aflam pe aceasta ruta, se va apela functia home din fisierul views.py
   path('about/', views.about, name='tweet_app-about'), #ruta localhost:8000/about/


   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  #<pk> este primary key a postarii. de exemplu,postarea 1, 2, 3.... Ne trebuie ca sa identificam postarea


   path('post/new/', PostCreateView.as_view(), name='post-create'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


   path('potiuni/', views.potiuni, name='tweet_app-potiuni'),  
   path('cristale/', views.cristale, name='tweet_app-cristale'),
   path('manifestari/', views.manifestari, name='tweet_app-manifestari'),  
   path('numerologie/', views.numerologie, name='tweet_app-numerologie'),
   path('ritualuri/', views.ritualuri, name='tweet_app-ritualuri'),  
   path('incantatii/', views.incantatii, name='tweet_app-incantatii'),
   path('blesteme/', views.blesteme, name='tweet_app-blesteme'),  

]
