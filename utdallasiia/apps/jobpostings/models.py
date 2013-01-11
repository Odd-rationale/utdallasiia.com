from django.contrib.auth.models import User
from django.db import models
from django_localflavor_us.models import USStateField

class JobPosting(models.Model):
    TYPE_CHOICES = (
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('IN', 'Internship'),
    )
    
    PENDING_STATUS = 0
    OPEN_STATUS = 1
    CLOSED_STATUS = 2
    STATUS_CHOICES = (
        (PENDING_STATUS, 'Pending'),
        (OPEN_STATUS, 'Open'),
        (CLOSED_STATUS, 'Closed'),
    )
    
    user = models.ForeignKey(User)
    job_title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    city = models.CharField(max_length=35)
    state = USStateField()
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    job_description = models.TextField()
    skill_experience = models.TextField()
    company_description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING_STATUS)
    
    job_title.help_text = 'e.g. Internal Auditor I'
    job_description.help_text = 'Include a brief job description, approximate start date, and a link or email to apply for the position.'    
    skill_experience.verbose_name = 'Desired skills and experience'
    
    def __unicode__(self):
        return self.job_title
