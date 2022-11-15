const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    historyApiFallback: true,
    proxy: {
      '/in2game': { 
        target: 'http://localhost:18080',
        ws: true,
        changeOrigin: true,
        logLevel: 'debug',
      }, 
    },
  },
  transpileDependencies: [
    'vuetify'
  ],
  lintOnSave: false, 
})
