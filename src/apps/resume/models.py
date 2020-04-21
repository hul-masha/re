from django.db import models


class Technology(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"#{self.pk}: {self.name!r}"

    # projects = models.ManyToManyField(projects)


class Project(models.Model):
    firm = models.TextField(null=True, blank=True)
    started_at = models.DateField(null=True, blank=True)
    finished_at = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    technologies = models.ManyToManyField(Technology, related_name="projects")
    # technology = models.TextField()
    # python = models.BooleanField()
    # django = models.BooleanField()


# tech = ...

# print(tech.tech)
class Responsibility(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="responsibilities"
    )  # on_delete=models.SET_NULL)
    summary = models.TextField()
