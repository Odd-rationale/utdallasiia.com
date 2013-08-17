from os.path import join
from uuid import uuid4

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from model_utils import Choices

from .filefields import ContentTypeRestrictedFileField
from .storage import smedia_storage


class Resume(models.Model):
    POSITION = Choices(
        'Full-time',
        'Intern',
        'Not Looking',
    )

    TRAVEL = Choices(
        '0%',
        '25%',
        '50%',
        '75%',
        '100%',
    )

    YES_OR_NO = Choices(
        'Yes',
        'No',
    )

    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        try:
            base = instance.user.member.netid
        except:
            base = 'resume'
        filename = "%s.%s.%s" % (base, uuid4(), ext)
        return join('resumebook', filename)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_accepted = models.BooleanField(default=False)
    position = models.CharField(max_length=20, choices=POSITION)
    travel = models.CharField(max_length=20, choices=TRAVEL)
    relocate = models.CharField(max_length=20, choices=YES_OR_NO)
    ia_course = models.CharField(max_length=20, choices=YES_OR_NO)
    it_position = models.CharField(max_length=20, choices=YES_OR_NO,
                                   default=YES_OR_NO.No)
    iia_membership = models.CharField(max_length=30, blank=True)
    isaca_membership = models.CharField(max_length=30, blank=True)
    acfe_membership = models.CharField(max_length=30, blank=True)
    resume = ContentTypeRestrictedFileField(
        upload_to=get_file_path,
        storage=smedia_storage,
        content_types=['application/pdf'],
        max_upload_size=1048576,
    )

    travel.verbose_name = 'Percentage of travel'
    relocate.verbose_name = 'Willing to relocate?'
    ia_course.verbose_name = 'Completed or enrolled in Internal Audit course?'
    it_position.verbose_name = 'IT position'
    iia_membership.verbose_name = 'IIA Membership Number'
    isaca_membership.verbose_name = 'ISACA Membership Number'
    acfe_membership.verbose_name = 'ACFE Membership Number'
    resume.help_text = ('Please submit as PDF. '
                        'Only one page (1024kb file limit).')

    def __unicode__(self):
        return self.user.last_name

    def clean(self):
        if ((self.iia_membership ==
             self.isaca_membership ==
             self.acfe_membership == '')):
            raise ValidationError('You must belong to at least one of the '
                                  'three professional organizations.')
