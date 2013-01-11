from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from utdallasiia.apps.resumebook.forms import ResumeForm
from utdallasiia.apps.resumebook.models import Resume

class ResumeBookView(ListView):
    queryset = Resume.objects.filter(student_status=Resume.ACCEPTED_STATUS).order_by('user__last_name')
    raise_exception = False
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.memberprofile.is_employer and request.user.resume.access_status == Resume.ACCEPTED_STATUS
        
        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            else:
                return render(request, 'resumebook/resume_access.html')
            
        return super(ResumeBookView, self).dispatch(request, *args, **kwargs)
        
class SubmitResume(UpdateView):
    form_class = ResumeForm
    success_url = reverse_lazy('dashboard_view')
    raise_exception = True
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.memberprofile.is_paid
        
        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            
        return super(SubmitResume, self).dispatch(request, *args, **kwargs)
    
    def get_object(self):
        return self.request.user.resume
    
    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.student_status = Resume.PENDING_STATUS
        resume.save()
        return super(SubmitResume, self).form_valid(form)

class DownloadResume(BaseDetailView):
    model = Resume
    raise_exception = True
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.is_superuser or request.user.memberprofile.is_employer
        
        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            
        return super(DownloadResume, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        resume = Resume.objects.get(pk=pk)
        if resume.resume:
            response = HttpResponse(resume.resume, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s%s.pdf' % (resume.user.first_name, resume.user.last_name)
            return response
        else:
            raise PermissionDenied
