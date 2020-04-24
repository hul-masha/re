from django.db import models as m


class Post(m.Model):
    tema = m.TextField(unique=True)
    post_text = m.TextField(null=True)
    likes = m.IntegerField(null=True, blank=True)
    data = m.DateField()

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self):
        return f"#Post{self.pk} -> {self.tema!r}"


class User(m.Model):
    name = m.TextField(unique=True)

    def __str__(self):
        return f"#User{self.pk} -> {self.name!r})"


class Comment(m.Model):
    author = m.ForeignKey(User, on_delete=m.CASCADE, related_name="users")
    message = m.TextField()
    post = m.ForeignKey(Post, on_delete=m.CASCADE, related_name="post")
    parent = m.ForeignKey(
        "Comment", on_delete=m.CASCADE, related_name="coments", blank=True, null=True
    )
    like = m.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"#Comment{self.pk} -> {self.message!r})"
