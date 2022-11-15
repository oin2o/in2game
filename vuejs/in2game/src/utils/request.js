import axios from 'axios'
const service = axios.create({
  baseURL: '/in2game',
  timeout: 5000, // request timeout
})

service.interceptors.response.use(
  response => {
    console.log('Response Success')
    console.log(response)
    return response
  },
  error => {
    return Promise.reject(error)
  }
)

export default service
