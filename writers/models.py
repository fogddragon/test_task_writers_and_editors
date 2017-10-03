# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    WRITER, EDITOR = 0, 1
    ROLES = [
        (WRITER, 'Writer'),
        (EDITOR, 'Editor')
    ]

    role = models.IntegerField(choices=ROLES, default=WRITER)
