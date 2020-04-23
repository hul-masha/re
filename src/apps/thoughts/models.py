from django.db import models as m


class Feedback(m.Model):
    name = m.TextField(unique=True)
    post_text = m.TextField(null=True, blank=True)
    message = m.TextField(null=True, blank=True)
    number = m.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Feedback Info"

    def __str__(self):
        return f"UserInfo(id={self.pk},name={self.name!r})"


class User(m.Model):
    name = m.TextField(unique=True)

    def __str__(self):
        return f"User(id={self.pk},name={self.name!r})"


class Comment(m.Model):
    author = m.ForeignKey(User, on_delete=m.CASCADE, related_name="users")
    message = m.TextField()
    post = m.ForeignKey(Feedback, on_delete=m.CASCADE, related_name="post")
    # parent = m.ForeignKey("Comment",
    #                     on_delete=m.CASCADE, related_name="coments",)
    like = m.IntegerField(null=True, blank=True)
