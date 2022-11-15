import Vue from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios'
import 'vuetify/dist/vuetify.min.css'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify);

Vue.config.productionTip = false

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

new Vue({
  router,
  vuetify: new Vuetify(),
  render: h => h(App)
}).$mount('#app')
