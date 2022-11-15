from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10, unique=True, primary_key=True)
    delYn = models.BooleanField(default=False)

    def __str__(self):
        return self.username + ':' + str(self.delYn)
