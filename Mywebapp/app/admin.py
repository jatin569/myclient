from django.contrib import admin

# Register your models here.
from app.models import signup,Photo
admin.site.register(signup)
admin.site.register(Photo)