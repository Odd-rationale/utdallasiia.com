from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class JobPostingApphook(CMSApp):
    name = _("Job Postings")
    urls = ["utdallasiia.apps.jobpostings.urls"]
    app_name = 'jobpostings'

apphook_pool.register(JobPostingApphook)