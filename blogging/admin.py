from django.contrib import admin
from .models import *

admin.site.register(BlogUser)
admin.site.register(Blog)
admin.site.register(Comment)