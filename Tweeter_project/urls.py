
# fisier unde sunt definite rutele valabile in proiect

###############################PAS 1 a codului####################### 
#   Cand punem o ruta in browser ( de exemplu http://localhost:8000/ sau http://localhost:8000/tweet_app/)
#   mai intai se va uita in acest urls.py din main project (Tweeter_project)

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from users_app import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),  #ruta. daca mergem pe ruta admin/ ne va trimite pe admin.site.urls
    path('register/',user_views.register, name='register'),
    path('profile/',user_views.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users_app/login.html'), name='login'),           #django are login si logout views deja facute
    path('logout/',auth_views.LogoutView.as_view(template_name='users_app/logout.html'), name='logout'),
    path('', include('tweet_app.urls')), #cand suntem pe ruta '' (localhost:8000), se va apela codul din urls.py din tweet_app
]



if settings.DEBUG:       #daca suntem in debug mode
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
