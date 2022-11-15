import random
import string

from rest_framework import viewsets, status
from rest_framework.response import Response

from .filters import GameFilter
from .models import Game
from .serializer import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filterset_class = GameFilter
    
    '''
     * 게임을 생성한다.
     *
     * @param : owner 게임 생성자
     *          gamename 게임이름(종류)
     * @return  201 게임생성 완료
     *          208 게임 valid 실패
     * 1. 전달받은 값 중, gamecode가 없는 경우(신규 생성 시), 숫자 + 대소문자 6자리로 생성하여 data에 추가한다.
     * 2. 객체 데이터의 유효성 검증 후, 게임을 생성한다.
     * 2.1. 유효성 검증이 실패한 경우, 오류를 출력한다.
    '''
    def create(self, request):
        # gamecode 값이 없는 경우, 생성하여 추가     
        if 'gamecode' not in request.data:
            # 1. 전달받은 값 중, gamecode가 없는 경우(신규 생성 시), 숫자 + 대소문자 6자리로 생성하여 data에 추가한다.
            # - 필수값인 경우, serialize에 포함되어야 하므로 대상 data(request data)에 serialize 전 추가
            request.data['gamecode'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        
        game = self.get_serializer(data=request.data)
        
        if game.is_valid():
            # 2. 객체 데이터의 유효성 검증 후, 게임을 생성한다.
            game.save()
            return Response(game.data, status=status.HTTP_201_CREATED)
        else:
            # 2.1. 유효성 검증이 실패한 경우, 오류를 출력한다.
            for field in game:
                print("Field Error:", field.name,  field.errors)
            return Response(status=status.HTTP_208_ALREADY_REPORTED)
