from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from .models import Profile



class UserInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class UserAdmin(UserAdmin):
    inlines = (UserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
