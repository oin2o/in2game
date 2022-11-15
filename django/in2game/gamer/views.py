from rest_framework import viewsets, status
from rest_framework.response import Response

from .filters import GamerFilter
from .models import Gamer
from .serializer import GamerSerializer


class GamerViewSet(viewsets.ModelViewSet):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer
    filterset_class = GamerFilter
    
    '''
     * 게임 참가자를 생성한다.
     *
     * @param : game 게임
     *          user 게임 참가자
     * @return  201 게임 참가자 생성 완료
     *          208 게임 참가자 valid 실패
     * 1. 게임 종류에 따른 참가인원이 초과된 경우, 메시지를 출력한다.
     * 2. 객체 데이터의 유효성 검증 후, 게임 참가자를 생성한다.
     * 2.1. 유효성 검증이 실패한 경우, 오류를 출력한다.
    '''
    def create(self, request):
        gamers = Gamer.objects.filter(game=request.data['game'])
        
        # 1. 게임 종류에 따른 참가인원이 초과된 경우, 메시지를 출력한다.
        # 참가인원 체크는 게임입장 후, 참가/관전 여부 선택시에 체크하는 것으로 변경
        '''
        if len(gamers) >= 8:
            return Response(status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
        elif request.data['gamename'] == 'davinci' and len(gamers) >= 4:
            return Response(status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
        '''
        
        gamer = self.get_serializer(data=request.data)
        
        if gamer.is_valid():
            # 2. 객체 데이터의 유효성 검증 후, 게임 참가자를 생성한다.
            gamer.save()
            return Response(gamer.data, status=status.HTTP_201_CREATED)
        else:
            # 2.1. 유효성 검증이 실패한 경우, 오류를 출력한다.
            for field in gamer:
                print("Field Error:", field.name,  field.errors)
            return Response(status=status.HTTP_208_ALREADY_REPORTED)
