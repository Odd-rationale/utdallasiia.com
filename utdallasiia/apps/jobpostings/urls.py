from django.conf.urls import patterns, include, url
from utdallasiia.apps.jobpostings.views import JobPostingView, JobPostingDetail, JobPostingUserView, CreateJobPosting, UpdateJobPosting, CloseJobPosting, DeleteJobPosting

urlpatterns = patterns('',
    url(r'^$', JobPostingView.as_view(), name='job_posting_view'),
    url(r'^(?P<pk>\d+)/$', JobPostingDetail.as_view(), name='job_posting_detail'),
    url(r'^user/$', JobPostingUserView.as_view(), name='job_posting_user_view'),
    url(r'^user/new/$', CreateJobPosting.as_view(), name='create_job_posting'),
    url(r'^user/(?P<pk>\d+)/$', UpdateJobPosting.as_view(), name='update_job_posting'),
    url(r'^user/(?P<pk>\d+)/close/$', CloseJobPosting.as_view(), name='close_job_posting'),
    url(r'^user/(?P<pk>\d+)/delete/$', DeleteJobPosting.as_view(), name='delete_job_posting'),
)
