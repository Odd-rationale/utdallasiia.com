from django import forms
from utdallasiia.apps.jobpostings.models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        exclude = (
            'user',
            'status',
        )