<template>
  <v-app id="app">
    <router-view/>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  mounted() {
    document.ontouchmove = function(event) {
      event.preventDefault()
    }
  },
}
</script>
<style lang="scss">
// Import Main styles for this application
@import 'assets/scss/common';
@media only screen and (orientation: landscape) {
  .portrait_only {
    display: none;
  }
}
</style>