from django.contrib import admin
from utdallasiia.apps.jobpostings.models import JobPosting
from utdallasiia.apps.jobpostings.forms import JobPostingForm

class JobPostingAdminForm(JobPostingForm):
    class Meta(JobPostingForm.Meta):
        exclude = ()

class JobPostingAdmin(admin.ModelAdmin):
    form = JobPostingAdminForm
    list_display = (
        'job_title',
        'company',
        'city',
        'state',
        'type',
        'status',
    )
    ordering = ('job_title',)
    list_filter = (
        'type',
        'status',
    )
    actions = (
        'mark_pending',
        'mark_open',
        'mark_closed',
    )
    search_fields = (
        'job_title',
        'company',
        'job_description',
        'skill_experience',
        'company_description',
    )
    
    # Define admin actions
    def mark_pending(self, request, queryset):
        queryset.update(status=JobPosting.PENDING_STATUS)
    mark_pending.short_description = 'Mark selected job postings as pending'
    
    def mark_open(self, request, queryset):
        queryset.update(status=JobPosting.OPEN_STATUS)
    mark_open.short_description = 'Mark selected job postings as open'
    
    def mark_closed(self, request, queryset):
        queryset.update(status=JobPosting.CLOSED_STATUS)
    mark_closed.short_description = 'Mark selected job postings as closed'

admin.site.register(JobPosting, JobPostingAdmin)
