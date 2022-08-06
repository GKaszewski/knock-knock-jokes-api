from django.contrib import admin

# Register your models here.
from jokes.models import Joke

admin.site.register(Joke)