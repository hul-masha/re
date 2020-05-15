from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

User = get_user_model()


class Post(models.Model):
    title = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    nr_likes = models.IntegerField(null=True, blank=True)
    nr_dislikes = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("blog:post", kwargs={"pk": str(self.pk)})

    # return  f"/blog/post/{self.pk}/"
    def upvote(self):
        if self.nr_likes is None:
            self.nr_likes = 0

        self.nr_likes += 1
        self.save()

    def downvote(self):
        if self.nr_dislikes is None:
            self.nr_dislikes = 0

        self.nr_dislikes += 1
        self.save()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    nr_likes = models.IntegerField(null=True, blank=True)
    nr_dislikes = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey(
        "Comment",
        on_delete=models.CASCADE,
        related_name="Comentsss",
        blank=True,
        null=True,
    )
    message = models.TextField()

    def upvote(self):
        if self.nr_likes is None:
            self.nr_likes = 0

        self.nr_likes += 1
        self.save()

    def downvote(self):
        if self.nr_dislikes is None:
            self.nr_dislikes = 0

        self.nr_dislikes += 1
        self.save()

    """@property
    def have_child(self):
        for p in Comment.objects.all():
            try:
                if p.parent == self:
                    return True
            except:
                ...
        return False"""

    @property
    def have_parent(self):
        try:
            if self.parent:
                return True
        except:
            return False

    @property
    def print_parent(self):
        z, l = [], self
        z.append(l)
        try:
            while l.parent:
                l = l.parent
                z.append(l)
            return z
        except AttributeError:
            z = [l]
            return z

    @property
    def print_first_childrens(self):
        z, l = [], self
        for p in Comment.objects.all():
            try:
                if p.parent == l:
                    z.append(p)
            except:
                ...
        return z
