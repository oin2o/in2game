from django.urls import include, path
from rest_framework import routers
from user import views as user_views
from game import views as game_views
from gamer import views as gamer_views


router = routers.DefaultRouter()
router.register('user', user_views.UserViewSet)
router.register('game', game_views.GameViewSet)
router.register('gamer', gamer_views.GamerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
