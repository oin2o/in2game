import request from '@/utils/request'

export default {
  isgame: function(game) {
    return request({
      url: '/game/' + game.gamecode,
      method: 'get',
    })
  },
  gamelistbystate: function(state) {
    return request({
      url: '/game/?state_lte=' + state + '&ordering=-created_at',
      method: 'get',
    })
  },
  creategame: function(gamename, user) {
    return request({
      url: '/game/',
      method: 'post',
      data: {
        owner: user.username,
        gamename: gamename,
      },
    })
  },
}