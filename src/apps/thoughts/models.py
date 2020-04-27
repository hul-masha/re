from django.db import models as m


class Post(m.Model):
    tema = m.TextField(unique=True)
    post_text = m.TextField(null=True)
    likes = m.IntegerField(null=True, blank=True)
    data = m.DateField()
    l, d, k = [], {}, []

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self):
        return f"#Post{self.pk} -> {self.tema!r}"

    def pr_dict(it, s=set()):
        for i in Post.d:
            # if i==it:
            if i not in s:
                Post.l.append((i[0], i[1]))  # ;print(i[0],i[1].message)
                s.add(i)
                for j in Post.d[i]:
                    if j not in Post.d:
                        Post.l.append((j[0], j[1]))  # ;print(j[0],j[1].message)
                    Post.pr_dict(j, s=s)

    def pri_root(self, li=[]):
        for p in Post.objects.all():
            li.append((p,))
            if p.post.count() > 0:
                for l in p.post.all():
                    y, x = Post.depth_for_root(Post.k, l)
                    if x == None and y == 2:
                        Post.k.append((0, l))
            for i in Post.k:
                li.extend(Post.pri(Post, i))
                Post.l = []
            Post.k = []
        return li

    def pri(self, el=None):
        n = []
        for p in Post.objects.all():
            if p.post.count() > 0:
                for l in p.post.all():
                    if l not in Post.k:
                        y, x = Post.depth(el[1], l)
                        if x == None:
                            continue
                        elif (y - 1, x) in Post.d:
                            Post.d[(y - 1, x)] += [(y, l)]
                        else:
                            Post.d[(y - 1, x)] = [(y, l)]
                if Post.d != {}:
                    Post.pr_dict(list(Post.d.keys())[0])
                else:
                    n.append(el)
        Post.d = {}
        if len(n) > 0 and len(Post.l) == 0:
            return [n[0]]
        else:
            return Post.l

    def depth_for_root(k, l):
        x, y = l, 1
        try:
            while l.parent not in k:
                l = l.parent
                y += 1
            return y, x.parent
        except AttributeError:
            return y, None

    def depth(k, l):
        x, y = l, 1
        try:
            while l.parent != k:
                l = l.parent
                y += 1
            return y, x.parent
        except AttributeError:
            return 0, None

    def li(self):
        return Post.pri_root(Post)


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
        return f"#Comment{self.pk} -> {self.message}: {self.author})"
