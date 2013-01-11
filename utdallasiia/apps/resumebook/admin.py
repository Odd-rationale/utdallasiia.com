from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from utdallasiia.apps.resumebook.models import Resume
from utdallasiia.apps.resumebook.forms import ResumeForm

class ResumeAdminForm(ResumeForm):
    class Meta(ResumeForm.Meta):
        exclude = ()
        widgets = {}
    
class ResumeAdmin(admin.ModelAdmin):
    form = ResumeAdminForm
    list_display = (
        'last_name',
        'first_name',
        'email',
        'netid',
        'phone_number',
        'student_status',
        'access_status',
        'resume_link',
    )
    ordering = ('user__last_name',)
    list_filter = (
        'student_status',
        'access_status',
        'user__memberprofile__is_student',
        'user__memberprofile__is_employer',
        'user__memberprofile__is_paid',
    )
    actions = (
        'add_to_resumebook',
        'remove_from_resumebook',
        'add_resumebook_access',
        'remove_resumebook_access',
    )
    search_fields = (
        'user__last_name',
        'user__first_name',
    )
    fieldsets = (
        (None, {
            'fields': ('user', 'position', 'travel', 'relocate', 'ia_course', 'it_position', 'iia_membership', 'isaca_membership', 'acfe_membership', 'resume')
        }),
        ('Status', {
            'classes': ('collapse',),
            'fields': ('student_status', 'access_status')
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
    
    def netid(self, obj):
        return obj.user.memberprofile.netid
    netid.admin_order_field = 'user__memberprofile__netid'
    
    def phone_number(self, obj):
        return obj.user.memberprofile.phone_number
    phone_number.admin_order_field = 'user__memberprofile__phone_number'
    
    def resume_link(self, obj):
        if obj.resume:
            return u'<a href="%s">File</a>' % reverse('download_resume', args=[obj.pk])
    resume_link.allow_tags = True
    resume_link.short_description = 'Resume'
    
    # Define admin actions
    def add_to_resumebook(self, request, queryset):
        queryset.update(student_status=Resume.ACCEPTED_STATUS)
    add_to_resumebook.short_description = 'Add selected users to resumebook'
    
    def remove_from_resumebook(self, request, queryset):
        queryset.update(student_status=Resume.NONE_STATUS)
    remove_from_resumebook.short_description = 'Remove selected users from resumebook'
    
    def add_resumebook_access(self, request, queryset):
        queryset.update(access_status=Resume.ACCEPTED_STATUS)
    add_resumebook_access.short_description = 'Grant access to selected users'
    
    def remove_resumebook_access(self, request, queryset):
        queryset.update(access_status=Resume.NONE_STATUS)
    remove_resumebook_access.short_description = 'Remove access from selected users'

admin.site.register(Resume, ResumeAdmin)
