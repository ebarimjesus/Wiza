

from django.contrib import admin
from .models import CustomUser


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'date_of_birth', 'profession', 'title', 'gender', 'nationality')
    list_filter = ('profession', 'gender', 'nationality')
    search_fields = ('user__username', 'user__email', 'phone_number')


admin.site.register(CustomUser)



