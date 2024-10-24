import os

from django.db import models
from django.contrib.auth.models import AbstractUser





class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    @property
    def filename(self):
        return os.path.basename(self.document.name)



