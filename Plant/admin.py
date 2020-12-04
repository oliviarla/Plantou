from django.contrib import admin

# Register your models here.
from Plant.models import Plant, User

admin.site.register(Plant)

admin.site.register(User)
