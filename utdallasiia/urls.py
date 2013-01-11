from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Setup LinkedIn login/logout urls
    url(r'', include('social_auth.urls')),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Setup Paypal IPN
    url(settings.PAYPAL_IPN_URL, include('paypal.standard.ipn.urls')),
    
    # Django Blog Zinnia
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    # Finally, load Django CMS urls
    url(r'^', include('cms.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.SMEDIA_URL, document_root=settings.SMEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
