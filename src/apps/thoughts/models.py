from django.db import models as m


class FeedbackInfo(m.Model):
    name = m.TextField(unique=True)
    message = m.TextField(null=True, blank=True)
    number = m.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Feedback Info"

    def __str__(self):
        return f"UserInfo(id={self.pk},name={self.name!r})"
