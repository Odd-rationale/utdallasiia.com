from django import forms
from django.db import models
from django.template.defaultfilters import filesizeformat
from south.modelsinspector import add_introspection_rules

add_introspection_rules([
  (
    [models.FileField],
    [],
    {
        "content_types": ["content_types", {}],
        "max_upload_size": ["max_upload_size", {}],
    },
  ),
], ["^utdallasiia\.libs\.resumefilefield\.ContentTypeRestrictedFileField"])

class ContentTypeRestrictedFileField(models.FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types.
          Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed
          for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")
        
        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):        
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
        
        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(
                        'Please keep filesize under %s. Current filesize %s' % 
                        (filesizeformat(self.max_upload_size),
                         filesizeformat(file._size))
                    )
            else:
                raise forms.ValidationError('Filetype not supported.')
        except AttributeError:
            pass        
            
        return data
