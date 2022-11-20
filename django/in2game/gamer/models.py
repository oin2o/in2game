from django.db import models

from user.models import User
from game.models import Game


class Gamer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.IntegerField(default=0, help_text="순번")
    status = models.IntegerField(default=0, help_text="0:게임대기, 1:관전, 2:레디")
    result = models.IntegerField(default=0, help_text="등수")

    def __str__(self):
        return str(self.game) + ':' + str(self.user) + ':' + str(self.position) + ':' + str(self.status) + ':' + str(self.result)
