from django.db import models

class Link(models.Model):
    link_title = models.CharField(max_length=200)
    original_url = models.CharField(max_length=200)

    def __str__(self):
        return self.link_title


class ChildLink(models.Model):
    parent_link = models.ForeignKey(Link, on_delete=models.CASCADE)
    link_title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.link_title
