# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):

    NEW, COMPLETED, TO_REVIEW, REVIEWED = 0, 1, 2, 3
    STATUSES = [
        (NEW, 'New'),
        (COMPLETED, 'Comleted'),
        (TO_REVIEW, 'To review'),
        (REVIEWED, 'Reviewed'),
    ]

    name = models.CharField(max_length=100, blank=False, null=False)
    link_to_article = models.URLField()
    creation_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('writers.User')
    status = models.IntegerField(choices=STATUSES, default=NEW)

    def __str__(self):
        return self.name