from .forms import SignUpEmailForm
from django.views.generic.edit import FormView


class EmailRegisterFormView(FormView):
    form_class = SignUpEmailForm
    success_url = "/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(EmailRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(EmailRegisterFormView, self).form_invalid(form)


