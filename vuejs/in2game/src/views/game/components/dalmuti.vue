<template>
  <v-container fluid>
    <v-row dense>
      <v-col cols="auto">
        <v-text-field v-model="message" dense></v-text-field>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col cols="auto">
        <v-card color="brown lighten-1" dark>
          <v-card-subtitle class="pt-3 pb-0">버튼 & Board 영역</v-card-subtitle>
          <v-card-actions class="pa-0">
            <v-container id="oneline-card-container">
              <v-row class="justify" dense>
              </v-row>
            </v-container>
          </v-card-actions>
        </v-card>
        <v-divider class="pa-4"></v-divider>
        <v-card class="align-self-end" color="brown lighten-0" dark>
          <v-card-subtitle class="pt-3 pb-0">카드 영역</v-card-subtitle>
          <v-card-actions class="pa-0">
            <v-container id="twoline-card-container">
              <v-row class="justify" dense>
              </v-row>
            </v-container>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
      message: "초기 메시지",
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