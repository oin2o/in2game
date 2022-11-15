import request from '@/utils/request'

export default {
  isuser: function(username) {
    return request({
      url: '/user/' + username,
      method: 'get',
    })
  },
  login: function(username) {
    return request({
      url: '/user/',
      method: 'post',
      data: {
        username: username,
        delYn: false,
      },
    })
  },
}