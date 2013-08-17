from django.db.models.signals import pre_save, post_delete

from .models import Resume


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


pre_save.connect(update_resume_file, sender=Resume)
post_delete.connect(delete_resume_file, sender=Resume)
