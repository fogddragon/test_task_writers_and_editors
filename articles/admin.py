# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):

    pass

admin.site.register(Article, ArticleAdmin)
