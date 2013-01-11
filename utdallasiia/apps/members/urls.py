from django.conf.urls import patterns, include, url
from utdallasiia.apps.members.views import DashboardView, UpdateMemberProfile, PayPalView

urlpatterns = patterns('',
    url(r'^$', DashboardView.as_view(), name='dashboard_view'),
    url(r'^select/(?P<slug>[-\w]+)/$', DashboardView.as_view(), name='dashboard_select'),
    url(r'^profile/$', UpdateMemberProfile.as_view(), name='update_profile'),
    url(r'^membership/$', PayPalView.as_view(), name='paypal_form'),
)
