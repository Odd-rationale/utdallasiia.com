from django.conf.urls import patterns, include, url
from utdallasiia.apps.resumebook.views import ResumeBookView, SubmitResume, DownloadResume

urlpatterns = patterns('',
    url(r'^$', ResumeBookView.as_view(), name='resume_book_view'),
    url(r'^submit/$', SubmitResume.as_view(), name='submit_resume'),
    url(r'^download/(?P<pk>\d+)/$', DownloadResume.as_view(), name='download_resume'),
)
