from django.contrib import admin
from .models import UserSignUp
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__","timestamp","updated"]
    class Meta():
        model = UserSignUp

admin.site.register(UserSignUp, SignUpAdmin)
