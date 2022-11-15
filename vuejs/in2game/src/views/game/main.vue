<template>
  <v-main id="gameBack" class="overflow-y-auto">
    <MenuSection v-bind:is_chat=true v-bind:menu_name=menu_name @call_back_menu="call_back_menu" />
    <v-container id="scrolling-app-bar" class="fill-height overflow-y-auto">
    </v-container>
  </v-main>
</template>
<script>
import MenuSection from '@/components/Menu';

export default {
  name: 'Game',
  components: {
    MenuSection,
  },
  data: () => {
    return {
      is_chat: false,
      menu_name: "none",
    };
  },
  created() {
    this.init();
  },
  methods : {
    init: async function() {
      if (!localStorage.getItem("in2game.user")) {
        this.$router.push({ path: '/' });
      }
    },
    call_back_menu: function(game){
    },
  },
};
</script>