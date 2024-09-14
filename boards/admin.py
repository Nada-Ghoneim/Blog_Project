from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Blog ,Post

admin.site.site_header ="Blogs admin panel" #to change heder at navbar
admin.site.site_title="Blogs admin panel"   #change title of the page



admin.site.register(Blog)
admin.site.register(Post)
admin.site.unregister(Group)   #to hide it from the page



