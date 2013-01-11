from django.contrib import admin
from django.contrib.auth.models import User
from utdallasiia.apps.members.models import MemberProfile
from utdallasiia.apps.members.forms import MemberProfileForm

class MemberProfileAdminForm(MemberProfileForm):
    class Meta(MemberProfileForm.Meta):
        exclude = ()

class MemberProfileAdmin(admin.ModelAdmin):
    form = MemberProfileAdminForm
    list_display = (
        'last_name',
        'first_name',
        'email',
        'is_student',
        'is_employer',
        'is_current',
        'is_paid',
    )
    ordering = ('user__last_name',)
    list_filter = (
        'is_student',
        'is_employer',
        'is_current',
        'is_paid',
    )
    actions = (
        'make_current',
        'make_not_current',
        'make_paid',
        'make_not_paid',
    )
    search_fields = (
        'user__last_name',
        'user__first_name',
    )
    fieldsets = (
        (None, {
            'fields': ('user', 'netid', 'phone_number', 'street_address', 'city', 'state', 'zip_code', 'tshirt_size', 'degree_plans', 'classification', 'graduation_month', 'graduation_year', 'citizen_resident')
        }),
        ('Status', {
            'classes': ('collapse',),
            'fields': ('is_student', 'is_employer', 'is_current', 'is_paid')
        }),
    )
    
    # Define list display
    def last_name(self, obj):
        return obj.user.last_name
    last_name.admin_order_field = 'user__last_name'
    
    def first_name(self, obj):
        return obj.user.first_name
    first_name.admin_order_field = 'user__first_name'
    
    def email(self, obj):
        return obj.user.email
    email.admin_order_field = 'user__email'
    email.short_description = 'e-mail addresses'
    
    # Define admin actions
    def make_current(self, request, queryset):
        queryset.update(is_current=True)
    make_current.short_description = 'Mark selected member profiles as current'
    
    def make_not_current(self, request, queryset):
        queryset.update(is_current=False)
    make_not_current.short_description = 'Mark selected member profiles as not current'
    
    def make_paid(self, request, queryset):
        queryset.update(is_paid=True)
    make_paid.short_description = 'Mark selected member profiles as paid'
    
    def make_not_paid(self, request, queryset):
        queryset.update(is_paid=False)
    make_not_paid.short_description = 'Mark selected member profiles as not paid'

admin.site.register(MemberProfile, MemberProfileAdmin)
