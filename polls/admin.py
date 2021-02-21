from django.contrib import admin

from .models import Question, User

admin.site.register(Question)
admin.site.register(User)