# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, FormView, DetailView

from articles.forms import ArticleForm
from articles.models import Article


class CreateArticleView(CreateView):
    template_name = "article/update_article.html"
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'pk': self.kwargs.get('pk')}, )


class UpdateArticleView(UpdateView):
    template_name = "article/create_article.html"
    form_class = ArticleForm
    queryset = Article.objects.all()

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'pk': self.kwargs.get('pk')}, )


class ArticleView(DetailView):
    template_name = "article/article.html"
    form_class = ArticleForm
    queryset = Article.objects.all()