# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Base(models.Model):

    class Meta:
        abstract = True

    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_updated = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    # updated_by = models.ForeignKey(settings.AUTH_USER_MODEL)


class InkDocument(Base):
    author = models.CharField(max_length=256, blank=True, null=True)
    authored_on = models.DateTimeField(blank=True, null=True)
    file = models.FileField(upload_to='ink_documents')
    thumbnail = models.FileField(upload_to='ink_documents_thumbnails', blank=True, null=True)


class InkDocumentAnnotation(Base):
    ink_document = models.ForeignKey('InkDocument')
    file = models.FileField(upload_to='annotations')
