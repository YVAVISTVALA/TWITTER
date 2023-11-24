from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Meep

admin.site.unregister(Group)


class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInLine]

#Unregister User
admin.site.unregister(User)

#User Re-Register

admin.site.register(User, UserAdmin)

# admin.site.register(Profile)

admin.site.register(Meep)