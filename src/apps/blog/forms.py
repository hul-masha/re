from django import forms

from apps.blog.models import Comment
from project.utils.xmodels import a


class ComentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            a(Comment.author): forms.HiddenInput,
            a(Comment.post): forms.HiddenInput,
            a(Comment.parent): forms.HiddenInput,
            a(Comment.message): forms.TextInput(attrs={"size": "30"}),
        }
        fields = [
            a(_f)
            for _f in (Comment.author, Comment.message, Comment.post, Comment.parent)
        ]
        """[
            "author",
            "message",
            "post",
        ] """  # [a(_f) for _f in (Comment.author, Comment.message, Comment.post)]
