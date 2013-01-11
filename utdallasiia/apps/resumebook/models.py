import os
from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models
from utdallasiia.libs.resumefilefield import ContentTypeRestrictedFileField
from utdallasiia.libs.smedia import smedia_storage

class Resume(models.Model):
    NONE_STATUS = 0
    PENDING_STATUS = 1
    ACCEPTED_STATUS = 2
    STATUS_CHOICES = (
        (NONE_STATUS, 'None'),
        (PENDING_STATUS, 'Pending'),
        (ACCEPTED_STATUS, 'Accepted'),
    )
    
    POSITION_CHOICES = (
        ('FT', 'Full-time'),
        ('IN', 'Intern'),
        ('NA', 'Not Looking'),
    )
    
    TRAVEL_CHOICES = (
        ('0', '0%'),
        ('25', '25%'),
        ('50', '50%'),
        ('75', '75%'),
        ('100', '100%'),
    )
    
    YES_OR_NO = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        try:
            base = instance.user.memberprofile.netid
        except:
            base = 'resume'
        filename = "%s.%s.%s" % (base, uuid4(), ext)
        return os.path.join('resumebook', filename)
    
    user = models.OneToOneField(User)
    last_modified = models.DateTimeField(auto_now=True)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    travel = models.CharField(max_length=3, choices=TRAVEL_CHOICES)
    relocate = models.CharField(max_length=1, choices=YES_OR_NO)
    ia_course = models.CharField(max_length=1, choices=YES_OR_NO)
    it_position = models.CharField(max_length=1, choices=YES_OR_NO, default='N')
    iia_membership = models.CharField(max_length=30, blank=True)
    isaca_membership = models.CharField(max_length=30, blank=True)
    acfe_membership = models.CharField(max_length=30, blank=True)
    resume = ContentTypeRestrictedFileField(
        upload_to=get_file_path,
        storage=smedia_storage,
        content_types=['application/pdf'],
        max_upload_size=1048576,
    )
    student_status = models.IntegerField(choices=STATUS_CHOICES, default=NONE_STATUS)
    access_status = models.IntegerField(choices=STATUS_CHOICES, default=NONE_STATUS)
    
    travel.verbose_name = 'Percentage of travel'
    relocate.verbose_name = 'Willing to relocate?'
    ia_course.verbose_name = 'Completed or enrolled in Internal Audit course?'
    it_position.verbose_name = 'IT position'
    iia_membership.verbose_name = 'IIA Membership Number'
    isaca_membership.verbose_name = 'ISACA Membership Number'
    acfe_membership.verbose_name = 'ACFE Membership Number'
    resume.help_text = 'Please submit as PDF. Only one page (1024kb file limit).'
    
    def __unicode__(self):
        return self.user.last_name