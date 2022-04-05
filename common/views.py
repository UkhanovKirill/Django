from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


class CommonContextMixin(SuccessMessageMixin):
    title = None
    date = datetime.now()

    def get_context_data(self, **kwargs):
        context = super(CommonContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CommonContextMixin, self).dispatch(request, *args, **kwargs)