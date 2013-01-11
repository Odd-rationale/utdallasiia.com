from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django_localflavor_us.models import PhoneNumberField, USStateField

class DegreePlan(models.Model):
    degree = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.degree

class MemberProfile(models.Model):
    CLASSIFICATION_CHOICES = (
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
    )
    
    GRAD_MONTH_CHOICES = (
        ('May', 'May'),
        ('Aug', 'August'),
        ('Dec', 'December'),
    )
    
    GRAD_YEAR_CHOICES = [
        (k, k) for k in range(date.today().year - 4, date.today().year + 8)
    ]
    
    TSHIRT_SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
        ('XXXL', 'Triple Extra Large'),
    )
    
    YES_OR_NO = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    user = models.OneToOneField(User)
    last_modified = models.DateTimeField(auto_now=True)
    netid = models.CharField(max_length=30)
    phone_number = PhoneNumberField()
    street_address = models.CharField(max_length=95)
    city = models.CharField(max_length=35)
    state = USStateField()
    zip_code = models.CharField(max_length=10)
    tshirt_size = models.CharField(max_length=4, choices=TSHIRT_SIZE_CHOICES)
    degree_plans = models.ManyToManyField(DegreePlan)
    classification = models.CharField(max_length=2, choices=CLASSIFICATION_CHOICES)
    graduation_month = models.CharField(max_length=3, choices=GRAD_MONTH_CHOICES)
    graduation_year = models.IntegerField(choices=GRAD_YEAR_CHOICES, null=True)
    citizen_resident = models.CharField(max_length=1, choices=YES_OR_NO)
    is_student = models.BooleanField()
    is_employer = models.BooleanField()
    is_current = models.BooleanField()
    is_paid = models.BooleanField()
    
    # Setup verbose names/labels
    netid.verbose_name = 'Net ID'
    netid.help_text = 'e.g. jxd032000'
    phone_number.help_text = 'e.g. XXX-XXX-XXXX'
    tshirt_size.verbose_name = 't-shirt size'
    degree_plans.verbose_name = 'degree plan(s)'
    degree_plans.help_text = 'Choose all that apply'
    citizen_resident.verbose_name = 'Are you a U.S. Citizen or Permanent Resident?'
    
    def __unicode__(self):
        return self.user.last_name
