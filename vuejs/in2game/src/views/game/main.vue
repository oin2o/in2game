<template>
  <v-main id="gameBack" class="overflow-y-auto">
    <MenuSection v-bind:is_chat=true v-bind:menu_name=menu_name @call_back_menu="call_back_menu" />
    <v-container id="scrolling-app-bar" class="fill-height">
      <v-row class="fill-height justify-end">
        <v-col class="pt-0" cols="auto">
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
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
import game_api from '@/api/game';
import gamer_api from '@/api/gamer';
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
      game: [],
      gamers: [],
    };
  },
  created() {
    this.init();
  },
  methods : {
    /**
     * 초기 로딩 시 게임 정보를 조회한다.
     *
     * 1. 로컬 스토리지의 사용자 정보 여부를 확인한다.
     * 1.1. 사용자 정보가 없는 경우, 로그인 페이지로 이동한다.
     * 2. 해당 게임의 현재 정보를 조회한다.
     * 3. 해당 게임의 플레이어 정보를 조회한다.
     */
    init: async function() {
      // 1. 로컬 스토리지의 사용자 정보 여부를 확인한다.
      if (!localStorage.getItem("in2game.user")) {
        // 1.1. 사용자 정보가 없는 경우, 로그인 페이지로 이동한다.
        this.$router.push({ path: '/' });
      }
      // 2. 해당 게임의 현재 정보를 조회한다.
      await game_api.isgame(JSON.parse(localStorage.getItem("in2game.game"))).then(response => {
        this.game = response.data;
      }).catch(error => {
        this.sys_error = true;
      });
      // 3. 해당 게임의 플레이어 정보를 조회한다.
      await gamer_api.gamerlistbygame(this.game).then(response => {
        this.gamers = response.data;
      }).catch(error => {
        this.sys_error = true;
      });
    },
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
    call_back_menu: function(game_name) {
    },
  },
};
</script>