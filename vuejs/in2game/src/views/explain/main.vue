<template>
  <v-main id="explainBack">
    <MenuSection v-bind:is_chat=is_chat v-bind:menu_name=menu_name @call_back_menu="call_back_menu" />
    <v-container id="scrolling-app-bar" class="fill-height overflow-y-auto">
      <v-row>
        <v-col>
          <v-card v-show="game_name == 'dalmuti'">
            <v-img src="~@/assets/images/cards/dalmuti/rule1.png" contain></v-img>
            <v-img src="~@/assets/images/cards/dalmuti/rule2.png" contain></v-img>
          </v-card>
          <v-card v-show="game_name == 'davinci'">
            <v-img src="~@/assets/images/cards/davinci/rule1.png" contain></v-img>
          </v-card>
          <v-card v-show="game_name == 'dixit'">
            <v-img src="~@/assets/images/cards/dixit/rule1.png" contain></v-img>
            <v-img src="~@/assets/images/cards/dixit/rule2.png" contain></v-img>
          </v-card>
          <v-card v-show="game_name == 'liar'">
            <v-img src="~@/assets/images/cards/liar/rule1.png" contain></v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
import MenuSection from '@/components/Menu';

export default {
  name: 'Explain',
  components: {
    MenuSection,
  },
  data: () => {
    return {
      is_chat: false,
      game_name: "none",
      menu_name: "all",
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
    call_back_menu: function(game_name){
      this.game_name = game_name;
    },
  },
};
</script>