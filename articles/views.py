# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, FormView, DetailView, ListView

from articles.forms import ArticleForm
from articles.models import Article
from writers.models import User


class CreateArticleView(CreateView):
    template_name = "article/create_article.html"
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateArticleView, self).form_valid(form)


class UpdateArticleView(UpdateView):
    template_name = "article/update_article.html"
    form_class = ArticleForm
    queryset = Article.objects.all()

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'pk': self.kwargs.get('pk')}, )

    def get_object(self, queryset=None):
        obj = super(UpdateArticleView, self).get_object(queryset)
        if obj.status not in [Article.TO_REVIEW, Article.REVIEWED] and self.request.user.role == User.EDITOR:
            raise HttpResponseForbidden
        return obj


class ArticleView(DetailView):
    template_name = "article/article.html"
    form_class = ArticleForm
    queryset = Article.objects.all()


class ArticleListView(ListView):
    template_name = "article/article_list.html"
    form_class = ArticleForm
    queryset = Article.objects.all()

    def get_queryset(self):
        if self.request.user.role == User.WRITER:
            queryset = self.queryset.filter(author=self.request.user)
        else:
            queryset = self.queryset.filter(status=Article.TO_REVIEW)
        return queryset.order_by('creation_date')
