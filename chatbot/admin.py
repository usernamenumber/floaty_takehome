from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Question, Answer
admin.site.register(Question)
admin.site.register(Answer)