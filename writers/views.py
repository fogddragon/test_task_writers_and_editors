# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.views.generic import FormView, RedirectView

from writers.forms import RegistrationForm


class IndexView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse('login')
        return reverse('article_list')


class RegistrationView(FormView):
    template_name = "registration/registration.html"
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user.set_password(form.cleaned_data['password'])
        user.save()
        return HttpResponseRedirect(self.get_success_url())
