import request from '@/utils/request'

export default {
  isgamer: function(game, user) {
    return request({
      url: '/gamer/?game=' + game.gamecode + '&user=' + user.username,
      method: 'get',
    })
  },
  gamerlistbygame: function(game) {
    return request({
      url: '/gamer/?game=' + game.gamecode + '&ordering=-created_at',
      method: 'get',
    })
  },
  gamerlistbyuser: function(user) {
    return request({
      url: '/gamer/?user=' + user.username,
      method: 'get',
    })
  },
  joingame: function(game, user) {
    return request({
      url: '/gamer/',
      method: 'post',
      data: {
        game: game.gamecode,
        user: user.username,
        gamename: game.gamename,
      },
    })
  },
}