from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ResumeBookApphook(CMSApp):
    name = _("Resume Book")
    urls = ["utdallasiia.apps.resumebook.urls"]
    app_name = 'resumebook'

apphook_pool.register(ResumeBookApphook)