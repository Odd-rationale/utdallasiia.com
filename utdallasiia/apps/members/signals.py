from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from paypal.standard.ipn.signals import payment_was_successful
from utdallasiia.apps.members.models import MemberProfile
        
def create_member_profile(sender, instance, created, **kwargs):
    if created:
        MemberProfile.objects.create(user=instance)

def paypal_ipn_receiver(sender, **kwargs):
    ipn_obj = sender
    
    if ipn_obj.test_ipn or ipn_obj.mc_gross != settings.PAYPAL_MC_GROSS:
        ipn_obj.flag = True
        ipn_obj.flag_info = 'Test IPN or amount mismatch'
        ipn_obj.save()

    elif ipn_obj.custom:
        try:
            user = User.objects.get(pk=ipn_obj.custom)
            user.memberprofile.is_paid = True
            user.memberprofile.save()
        except:
            return
        
post_save.connect(create_member_profile, sender=User)
payment_was_successful.connect(paypal_ipn_receiver)
