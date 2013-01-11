from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from paypal.standard.forms import PayPalPaymentsForm
from utdallasiia.apps.members.forms import MemberProfileForm
from utdallasiia.apps.members.models import MemberProfile

class DashboardView(TemplateView):
    template_name = 'members/members_dashboard.html'
    slug_url_kwarg = 'slug'
    
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        if slug is not None:
            if slug == 'student':
                request.user.memberprofile.is_student = True
                request.user.memberprofile.save()
            elif slug == 'employer':
                request.user.memberprofile.is_employer = True
                request.user.memberprofile.save()
                request.user.resume.access_status = 1 # PENDING_STATUS
                request.user.resume.save()
            return redirect('dashboard_view')

        return super(DashboardView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
    
class UpdateMemberProfile(UpdateView):
    form_class = MemberProfileForm
    success_url = reverse_lazy('dashboard_view')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateMemberProfile, self).dispatch(request, *args, **kwargs)
    
    def get_object(self):
        return self.request.user.memberprofile
    
    def form_valid(self, form):
        member_profile = form.save(commit=False)
        member_profile.is_current = True
        member_profile.save()
        return super(UpdateMemberProfile, self).form_valid(form)
    
class PayPalView(TemplateView):
    template_name = 'members/members_paypal.html'
    raise_exception = True
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        has_permission = request.user.memberprofile.is_current
        
        if not has_permission:  # If the user lacks the permission
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response.
            
        return super(PayPalView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": "0.01",
            "item_name": "UT Dallas IIA Membership",
            "invoice": "iia-membership",
#            "notify_url": "http://%s%s" % (self.request.get_host(), reverse_lazy('paypal-ipn')),
            "notify_url": "http://%s%s" % ('oddrationale.pagekite.me', reverse_lazy('paypal-ipn')),
            "return_url": "http://%s%s" % (self.request.get_host(), reverse_lazy('dashboard_view')),
            "cancel_return": "http://%s%s" % (self.request.get_host(), reverse_lazy('dashboard_view')),
            "custom": self.request.user.pk,
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        context = super(PayPalView, self).get_context_data(**kwargs)
        context['form'] = form
        return context
