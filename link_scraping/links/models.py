from django.db import models

class ParentLink(models.Model):
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.url


class ChildLink(models.Model):
    parent_link = models.ForeignKey(ParentLink, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.url

class GrandChildLink(models.Model):
    parent_link = models.ForeignKey(ChildLink, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.url
