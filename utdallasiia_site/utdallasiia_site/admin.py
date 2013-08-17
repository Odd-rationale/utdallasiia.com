from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from members.models import Member
from resumes.models import Resume


class MemberInline(admin.StackedInline):
    model = Member
    suit_classes = 'suit-tab suit-tab-profile'


class ResumeInline(admin.StackedInline):
    model = Resume
    max_num = 1
    suit_classes = 'suit-tab suit-tab-resume'


class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'last_name',
        'first_name',
        'email',
    )
    ordering = ('last_name',)
    inlines = (
        MemberInline,
        ResumeInline,
    )
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-user',),
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'classes': ('suit-tab suit-tab-user',),
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'classes': ('collapse', 'suit-tab suit-tab-user',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'classes': ('collapse', 'suit-tab suit-tab-user',),
            'fields': ('last_login', 'date_joined')
        }),
    )
    suit_form_tabs = (
        ('user', 'User'),
        ('profile', 'Profile'),
        ('resume', 'Resume'),
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
