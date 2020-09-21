from django.db import models
import uuid

class ParentLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.url

class ChildLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    parent_link = models.ForeignKey(ParentLink, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.url

class GrandchildLink(models.Model):
    child_link = models.ForeignKey(ChildLink, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.url
