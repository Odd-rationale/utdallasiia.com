from django import forms
from utdallasiia.apps.resumebook.models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = (
            'user',
            'student_status',
            'access_status',
            'it_position',
        )
        widgets = {
            'resume': forms.widgets.FileInput,
        }
        
    def clean(self):
        cleaned_data = super(ResumeForm, self).clean()
        if cleaned_data['iia_membership'] == cleaned_data['iia_membership'] == cleaned_data['iia_membership'] == '':
            raise forms.ValidationError('You must belong to at least one of the three professional organizations.')
        else:
            return cleaned_data
