from django.contrib import admin
from .models import Results, Team, Fixtures

# Register your models here.
admin.site.register([Results, Team, Fixtures])