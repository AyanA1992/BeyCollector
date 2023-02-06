from django.contrib import admin

# Register your models here.
from .models import Beyonce, Shows, Tour, Photo

# register
admin.site.register(Beyonce)
admin.site.register(Shows)
admin.site.register(Tour)
admin.site.register(Photo)