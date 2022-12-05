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
      url: '/gamer/?game=' + game.gamecode + '&ordering=-status,position',
      method: 'get',
    })
  },
  gamerlistbyuser: function(user) {
    return request({
      url: '/gamer/?user=' + user.username + '&ordering=-game__created_at',
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
  deletegamer: function(gamer) {
    return request({
      url: '/gamer/' + gamer.id,
      method: 'delete',
    })
  },
}