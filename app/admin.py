from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Todo)
admin.site.register(Blogs)
admin.site.register(Comment)