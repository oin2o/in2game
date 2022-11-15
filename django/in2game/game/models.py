from django.db import models

from user.models import User


class Game(models.Model):
    gamecode = models.CharField(max_length=6, unique=True, primary_key=True, help_text="게임코드")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gamename = models.CharField(max_length=50, help_text="게임이름")
    chapter = models.IntegerField(default=0, help_text="게임 라운드")
    state = models.IntegerField(default=0, help_text="0:게임대기, 1:게임중, 2:결과확인, 9:게임종료")
    stage = models.IntegerField(default=0, help_text="0:게임준비, 1:세금, 2:단어선택, 3:투표, 4:마지막찬스")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gamecode + ':' + str(self.owner) + ':' + str(self.chapter) + ':' + str(self.state) + ':' + str(self.stage) + ':' + str(self.created_at) + ':' + str(self.updated_at)
