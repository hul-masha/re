from django.db import models


class Technology(models.Model):
    name = models.TextField(unique=True)
    version = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        version = f" {self.version}" if self.version else ""
        return f"#{self.pk} {self.name!r} : {version}"

    # projects = models.ManyToManyField(projects)
    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ("name",)
        # constraints = (
        #   models.UniqueConstraint(
        #      fields=("name", "version"), name="unique_name_version_v01"
        # ),
        # )
