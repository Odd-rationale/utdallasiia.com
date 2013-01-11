from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class MembersApphook(CMSApp):
    name = _("Members")
    urls = ["utdallasiia.apps.members.urls"]
    app_name = 'members'

apphook_pool.register(MembersApphook)