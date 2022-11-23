<template>
  <v-main id="gameBack" class="overflow-y-auto">
    <MenuSection v-bind:is_chat=true v-bind:menu_name=menu_name @call_back_menu="call_back_menu" />
    <v-container id="scrolling-app-bar" fluid>
      <v-row class="align-self-start justify-end">
        <v-col cols="auto">
          <HeaderSection v-bind:game=game v-bind:gamers=gamers />
        </v-col>
      </v-row>
    </v-container>
    <DalmutiSection v-if="game.gamename == 'dalmuti'" v-bind:game=game v-bind:gamers=gamers />
  </v-main>
</template>
<script>
import game_api from '@/api/game';
import gamer_api from '@/api/gamer';
import MenuSection from '@/components/Menu';
import HeaderSection from './components/header';
import DalmutiSection from './components/dalmuti';

export default {
  name: 'Game',
  components: {
    MenuSection,
    HeaderSection,
    DalmutiSection,
  },
  data: () => {
    return {
      is_chat: false,
      menu_name: "none",
      game: {},
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
    call_back_menu: function(game_name) {
    },
  },
};
</script>