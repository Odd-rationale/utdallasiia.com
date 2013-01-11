from django import forms
from utdallasiia.apps.members.models import MemberProfile

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        widgets = {'degree_plans': forms.widgets.CheckboxSelectMultiple}
        exclude = (
            'user',
            'is_student',
            'is_employer',
            'is_current',
            'is_paid',
        )
