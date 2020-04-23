from typing import Iterable

from django.db import models


"""class Technology(models.Model):
    name = models.TextField(unique=True)
    version = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"#{self.pk}: {self.name!r}"

    # projects = models.ManyToManyField(projects)"""


class Project(models.Model):
    name = models.TextField(unique=True)
    started_at = models.DateField(null=True, blank=True)
    finished_at = models.DateField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    achievements = models.TextField(null=True, blank=True)
    responsibilities = models.TextField(null=True, blank=True)
    firm = models.ForeignKey("Firm", on_delete=models.CASCADE, related_name="projects")
    technologies = models.ManyToManyField(
        "Technology", related_name="projects", blank=True
    )
    # technology = models.TextField()
    # python = models.BooleanField()
    # django = models.BooleanField()
    @property
    def achievemen(self) -> Iterable[str]:
        return tuple(
            filter(bool, (_r.strip() for _r in (self.achievements or "").split("\n")))
        )

    @property
    def responsibil(self) -> Iterable[str]:
        return tuple(
            filter(
                bool, (_r.strip() for _r in (self.responsibilities or "").split("\n")),
            )
        )

    def __str__(self):
        return f"#{self.pk} {self.firm.name} -> {self.name!r}"

    class Meta:
        verbose_name_plural = "Projects"
        ordering = (
            "-started_at",
            "name",
        )


# tech = ...

# print(tech.tech)
"""class Responsibility(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="responsibilities"
    )  # on_delete=models.SET_NULL)
    summary = models.TextField()"""
