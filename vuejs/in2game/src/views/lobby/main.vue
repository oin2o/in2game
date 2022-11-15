<template>
  <v-main id="lobbyBack">
    <MenuSection v-bind:is_chat=is_chat v-bind:menu_name=menu_name @call_back_menu="call_back_menu" />
    <v-container id="scrolling-app-bar" class="fill-height">
      <v-row>
        <v-col cols="auto">
          <v-card color="brown lighten-1" dark>
            <v-card-subtitle class="pt-3 pb-0">참가 가능 게임</v-card-subtitle>
            <v-card-actions class="pa-0">
              <v-container id="oneline-card-container">
                <v-row class="justify" dense>
                  <v-col class="pa-1" cols="3" v-for="(game, index) in game_list" v-bind:key="index">
                    <GameSection v-bind:game=game @join_game="join_game" />
                  </v-col>
                </v-row>
              </v-container>
            </v-card-actions>
          </v-card>
          <v-divider class="pa-4"></v-divider>
          <v-card color="brown lighten-0" dark>
            <v-card-subtitle class="pt-3 pb-0">참가 중 게임</v-card-subtitle>
            <v-card-actions class="pa-0">
              <v-container id="twoline-card-container">
                <v-row class="justify" dense>
                  <v-col class="pa-1" cols="3" v-for="(game, index) in game_list_by_user" v-bind:key="index">
                    <GameSection v-bind:game=game.game @join_game="join_game" />
                  </v-col>
                </v-row>
              </v-container>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <DialogSection v-bind:biz_error=biz_error v-bind:cre8_game=cre8_game v-bind:overcrowding=overcrowding v-bind:sys_error=sys_error v-bind:game_name=game_name @close_dialog="close_dialog" @create_game="create_game" />
  </v-main>
</template>
<script>
import game_api from '@/api/game';
import gamer_api from '@/api/gamer';
import MenuSection from '@/components/Menu';
import GameSection from '@/components/Game';
import DialogSection from './components/dialog';

export default {
  name: 'Lobby',
  components: {
    MenuSection,
    GameSection,
    DialogSection,
  },
  data: () => {
    return {
      biz_error: false,
      cre8_game: false,
      is_chat: false,
      overcrowding: false,
      sys_error: false,
      game_name: "none",
      menu_name: "all",
      game_list: [],
      game_list_by_user: [],
      max_gamers: { 'dalmuti': 8, 'dixit': 8, 'davinci': 4, 'liar': 8},
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
     * 2. 상태코드가 게임대기, 게임중, 결과확인(state 코드 2 이하)인 게임 정보를 조회한다.
     */
    init: async function() {
      // 1. 로컬 스토리지의 사용자 정보 여부를 확인한다.
      if (!localStorage.getItem("in2game.user")) {
        // 1.1. 사용자 정보가 없는 경우, 로그인 페이지로 이동한다.
        this.$router.push({ path: '/' });
      }
      // 2. 상태코드가 게임대기(state 코드 0 이하)인 게임 정보를 조회한다.
      await game_api.gamelistbystate(0).then(response => {
        this.game_list = response.data;
      }).catch(error => {
        this.sys_error = true;
      });
      // 3. 참가중인 게임 정보를 조회한다.
      await gamer_api.gamerlistbyuser(JSON.parse(localStorage.getItem("in2game.user"))).then(response => {
        this.game_list_by_user = response.data;
      }).catch(error => {
        this.sys_error = true;
      });
    },
    /**
     * 게임을 생성한다.선을 정하기 위해 카드를 선택한다.
     *
     * 1. 신규 게임을 생성한다.
     * 2. 생성된 게임 정보를 로컬 스토리지에 저장한다.
     * 3. owner 사용자를 게임 플레이어 중 1명으로 추가한다.
     */
    create_game: async function(){
      this.cre8_game = false;
      let response;
      
      // 1. 신규 게임을 생성한다.
      response = await game_api.creategame(this.game_name, JSON.parse(localStorage.getItem("in2game.user")));
      
      if (response.status == 201) {
        // 2. 생성된 게임 정보를 로컬 스토리지에 저장한다.
        localStorage.setItem("in2game.game", JSON.stringify(response.data));
        // 3. owner 사용자를 게임 플레이어로 추가한다.
        this.join_game(JSON.parse(localStorage.getItem("in2game.game")));
      } else if (response.status == 208) {
        this.biz_error = true;
      } else {
        this.sys_error = true;
      }  
    },
    /**
     * 사용자를 게임 플레이어로 추가한다.
     *
     * @param : gamecode 게임코드
     * 1. 해당 게임의 플레이어 여부를 확인한다.
     * 1.1. 기존 플레이어가 아닌 경우, 참가 가능 인원을 확인한다.
     * 1.1.1. 참가 가능한 경우, 플레이어 추가 후, 게임으로 이동한다.
     * 1.1.2. 게임의 참가인원이 초과된 경우, 메시지를 출력한다.
     * 1.2. 기존 플레이어인 경우, 게임으로 이동한다.
     * 1.3. 해당 플레이어 정보가 여러개인 경우, 시스템 오류
     */
    join_game: async function(game){
      let response;

      // 1. 해당 게임의 플레이어 여부를 확인한다.
      response = await gamer_api.isgamer(game, JSON.parse(localStorage.getItem("in2game.user")));

      if (response.data.length == 0) {
        /* 참가인원 체크는 게임입장 후, 참가/관전 여부 선택시에 체크하는 것으로 변경
        // 1.1. 기존 플레이어가 아닌 경우, 참가 가능 인원을 확인한다.
        response = await gamer_api.gamerlistbygame(game);

        if (response.data.length < this.max_gamers[game.gamename]) {
          // 1.1.1. 참가 가능한 경우, 플레이어 추가 후, 게임으로 이동한다.
          response = await gamer_api.joingame(game, JSON.parse(localStorage.getItem("in2game.user")));

          if (response.status == 201 || response.status == 208) {
            this.$router.push({ path: 'game' });
          } else if (response.status == 413) {
            this.overcrowding = true;
          } else {
            this.sys_error = true;
          }  
        } else {
          // 1.1.2. 게임의 참가인원이 초과된 경우, 메시지를 출력한다.
          this.overcrowding = true;
        }
        */

        // 1.1.1. 참가 가능한 경우, 플레이어 추가 후, 게임으로 이동한다.
        response = await gamer_api.joingame(game, JSON.parse(localStorage.getItem("in2game.user")));

        if (response.status == 201 || response.status == 208) {
          this.$router.push({ path: 'game' });
        } else {
          this.sys_error = true;
        }  
      } else if (response.data.length == 1) {
        // 1.2. 기존 플레이어인 경우, 게임으로 이동한다.
        this.$router.push({ path: 'game' });
      } else {
        // 1.3. 해당 플레이어 정보가 여러개인 경우, 시스템 오류
        this.sys_error = true;
      }
    },
    call_back_menu: function(game_name){
      this.cre8_game = true;
      this.game_name = game_name;
    },
    close_dialog: function(){
      this.biz_error = false;
      this.cre8_game = false;
      this.overcrowding = false;
      this.sys_error = false;
    },
  },
};
</script>