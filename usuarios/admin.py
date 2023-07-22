from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as adm_auth_django
from .forms import UserChangeForm, UserCreationForm

@admin.register(Users)
class UsersAdmin(adm_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = adm_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )