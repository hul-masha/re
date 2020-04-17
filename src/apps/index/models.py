from django.db import models as m

# Create your models here.
class UserInfo(m.Model):
    name = m.TextField(unique=True)
    greeting = m.TextField(null=True, blank=True)
    age = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "User Info"  #выставл прав имя а не джанго дичку

        def __str__(self):
            return f"UserInfo(id={self.pk},name={self.name!r})" #not work

#a = UserInfo()
#b = UserInfo()
#print(a.name); print(b.name)
#a.name=2
#print(b.name)