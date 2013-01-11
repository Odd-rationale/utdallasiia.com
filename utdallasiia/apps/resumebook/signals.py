from django.db.models.signals import post_delete, pre_save, post_save
from django.contrib.auth.models import User
from utdallasiia.apps.resumebook.models import Resume
        
def create_resume(sender, instance, created, **kwargs):
    if created:
        Resume.objects.create(user=instance)
           
def update_resume_file(sender, instance, **kwargs):
    try:
        current_resume = sender.objects.get(pk=instance.pk).resume
        if instance.resume != current_resume:
            current_resume.delete(save=False)
    except:
        return
        
def delete_resume_file(sender, instance, **kwargs):
    try:
        instance.resume.delete(save=False)
    except:
        return
        
post_save.connect(create_resume, sender=User)
pre_save.connect(update_resume_file, sender=Resume)
post_delete.connect(delete_resume_file, sender=Resume)
