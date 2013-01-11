from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic.detail import BaseDetailView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from utdallasiia.apps.jobpostings.forms import JobPostingForm
from utdallasiia.apps.jobpostings.models import JobPosting

class JobPostingView(ListView):
    queryset = JobPosting.objects.exclude(status=JobPosting.PENDING_STATUS).order_by('job_title')

class JobPostingDetail(DetailView):
    model = JobPosting
    raise_exception = False
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.memberprofile.is_employer or request.user.memberprofile.is_paid
        
        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return render(request, 'jobpostings/jobposting_access.html')
            
        return super(JobPostingDetail, self).dispatch(request, *args, **kwargs)

class JobPostingUserView(ListView):
    raise_exception = True
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.memberprofile.is_employer
        
        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            
        return super(JobPostingUserView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return JobPosting.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(JobPostingUserView, self).get_context_data(**kwargs)
        context['user_view'] = True
        return context

class CreateJobPosting(CreateView):
    form_class = JobPostingForm
    template_name = 'jobpostings/jobposting_form.html'
    success_url = reverse_lazy('job_posting_user_view')
    raise_exception = True
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.memberprofile.is_employer
        
        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.

        return super(CreateJobPosting, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        jobposting = form.save(commit=False)
        jobposting.user = self.request.user
        jobposting.save()
        return super(CreateJobPosting, self).form_valid(form)

class UpdateJobPosting(UpdateView):
    form_class = JobPostingForm
    template_name = 'jobpostings/jobposting_form.html'
    success_url = reverse_lazy('job_posting_user_view')
    raise_exception = True
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.memberprofile.is_employer
        
        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.

        return super(UpdateJobPosting, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UpdateJobPosting, self).get_context_data(**kwargs)
        context['update_view'] = True
        return context
    
    def get_queryset(self):
        return JobPosting.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        jobposting = form.save(commit=False)
        jobposting.status = JobPosting.PENDING_STATUS
        jobposting.save()
        return super(UpdateJobPosting, self).form_valid(form)

class CloseJobPosting(BaseDetailView):
    raise_exception = True

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.memberprofile.is_employer
        
        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.

        return super(CloseJobPosting, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return JobPosting.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = JobPosting.CLOSED_STATUS
        self.object.save()
        return redirect('job_posting_user_view')

class DeleteJobPosting(DeleteView):
    success_url = reverse_lazy('job_posting_user_view')
    raise_exception = True
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.memberprofile.is_employer
        
        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.

        return super(DeleteJobPosting, self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return JobPosting.objects.filter(user=self.request.user)