<template>
  <v-main>
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
          <v-chip class="mr-1" color="white" v-bind="attrs" v-on="on" style="z-index:2;" label small>
          <v-icon left small>mdi-human-queue</v-icon>
          참가자
          </v-chip>
      </template>
      <v-list dense>
          <v-list-item v-for="(gamer, i) in gamers" :key="i">
          <v-list-item-title id="shadow-text">{{ gamer.user.username }}</v-list-item-title>
          <v-list-item-subtitle>{{ gamer.status }}</v-list-item-subtitle>
          </v-list-item>
      </v-list>
    </v-menu>
    <v-chip color="white" @click="generatelink()" style="z-index:2;" label small>
      <v-icon left small>mdi-download-box</v-icon>
      {{ this.game.gamecode }}
    </v-chip>
  </v-main>
</template>
<script>
export default {
  name: 'GameHeader',
  props: {
    game: Object,
    gamers: Array,
  },
  data: () => {
    return {
    };
  },
  methods : {
    /**
     * 게임의 Link를 생성한다.
     *
     * 1. 게임의 Link를 ClipBoard로 복사한다.
     */
    generatelink: function() {
      // 1. 게임의 Link를 ClipBoard로 복사한다.
      navigator.clipboard.writeText(window.location.origin + '/login?gamecode=' + this.game.gamecode);
      this.$dialog.alert_dialog("게임 링크 생성", this.game.gamecode + " 게임의 링크가 복사되었습니다.");
    },
  },
};
</script>