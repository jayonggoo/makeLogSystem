from django.contrib import admin

from .models import Question, User, RegisterModel

admin.site.register(Question)
admin.site.register(User)
admin.site.register(RegisterModel)

# Register your models here.
