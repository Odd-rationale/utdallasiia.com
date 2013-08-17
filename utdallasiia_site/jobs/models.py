from django.conf import settings
from django.db import models

from django_localflavor_us.models import USStateField
from model_utils import Choices


class Job(models.Model):
    STATUS = Choices(
        'Pending',
        'Open',
        'Closed',
    )

    TYPE = Choices(
        'Full-time',
        'Part-time',
        'Internship',
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    status = models.CharField(max_length=30, choices=STATUS,
                              default=STATUS.Pending)
    job_title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    city = models.CharField(max_length=35)
    state = USStateField()
    position = models.CharField(max_length=30, choices=TYPE)
    job_description = models.TextField()
    skill_experience = models.TextField()
    company_description = models.TextField()

    job_title.help_text = 'e.g. Internal Auditor I'
    job_description.help_text = ('Include a brief job description, '
                                 'approximate start date, and a link or '
                                 'email to apply for the position.')
    skill_experience.verbose_name = 'Desired skills and experience'

    def __unicode__(self):
        return self.job_title
