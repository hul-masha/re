from django.db import models


class Firm(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk}: {self.name}"

    class Meta:
        ordering = ("name",)
