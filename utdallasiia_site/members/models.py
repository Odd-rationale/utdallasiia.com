from datetime import date

from django.conf import settings
from django.db import models
from django_localflavor_us.models import PhoneNumberField, USStateField

from model_utils import Choices


class DegreePlan(models.Model):
    degree = models.CharField(max_length=30)

    def __unicode__(self):
        return self.degree


class Member(models.Model):
    CLASSIFICATION = Choices(
        'Full-time',
        'Part-time',
    )

    YES_OR_NO = Choices(
        'Yes',
        'No',
    )

    GRAD_MONTH = Choices(
        'May',
        'August',
        'December'
    )

    GRAD_YEAR = [
        (k, k) for k in range(date.today().year - 4, date.today().year + 8)
    ]

    TSHIRT_SIZE = Choices(
        'Small',
        'Medium',
        'Large',
        'Extra Large',
        'Double Extra Large',
        'Triple Extra Large',
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    netid = models.CharField(max_length=30)
    phone_number = PhoneNumberField()
    street_address = models.CharField(max_length=95)
    city = models.CharField(max_length=35)
    state = USStateField()
    zip_code = models.CharField(max_length=10)
    tshirt_size = models.CharField(max_length=20, choices=TSHIRT_SIZE)
    degree_plans = models.ManyToManyField(DegreePlan)
    classification = models.CharField(max_length=20, choices=CLASSIFICATION)
    graduation_month = models.CharField(max_length=20, choices=GRAD_MONTH)
    graduation_year = models.IntegerField(choices=GRAD_YEAR)
    citizen_resident = models.CharField(max_length=20, choices=YES_OR_NO)

    # Setup verbose names/labels
    netid.verbose_name = 'Net ID'
    netid.help_text = 'e.g. jxd032000'
    phone_number.help_text = 'e.g. XXX-XXX-XXXX'
    tshirt_size.verbose_name = 't-shirt size'
    degree_plans.verbose_name = 'degree plan(s)'
    degree_plans.help_text = 'Choose all that apply'
    citizen_resident.verbose_name = ('Are you a U.S. Citizen or '
                                     'Permanent Resident?')

    def __unicode__(self):
        return self.user.last_name
