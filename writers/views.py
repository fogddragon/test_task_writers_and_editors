# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from writers.forms import RegistrationForm


class IndexView(TemplateView):
    template_name = "index.html"


class RegistrationView(FormView):
    template_name = "registration/registration.html"
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user.set_password(form.cleaned_data['password'])
        user.save()
        return HttpResponseRedirect(self.get_success_url())
