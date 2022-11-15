import request from '@/utils/request'

export default {
  gamerlist: function(game) {
    return request({
      url: '/gamer/?game=' + game.gamecode,
      method: 'get',
    })
  },
  isgamer: function(game, user) {
    return request({
      url: '/gamer/?game=' + game.gamecode + '&user=' + user.username,
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