
#fisier cu modelele disponibile in interfata adminului


from django.contrib import admin
from .models import Post
# Register your models here pentru ca acestea sa apara in django administration



admin.site.register(Post)   #va aparea in django administration in  tweet_app -> post
