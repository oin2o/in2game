<template>
  <v-main id="loginBack">
    <v-container class="fill-height">
      <v-row class="fill-height" dense justify="center">
        <v-col class="mb-12" align-self="end" cols="auto">
          <v-form v-show="is_hidden">
            <v-container>
              <v-row align="center">
                <v-col cols="9">
                  <v-text-field v-model="username" counter maxlength="10" label="이름을 입력하세요." required />
                </v-col>
                <v-col cols="3">
                  <v-btn @click="login" icon>
                    <v-icon x-large color="orange accent-3">mdi-language-go</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
          <v-btn v-show="!is_hidden" @click="is_hidden = !is_hidden" icon>
            <v-icon x-large color="pink accent-3">mdi-fingerprint</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
import user_api from '@/api/user';
import game_api from '@/api/game';
import gamer_api from '@/api/gamer';

export default {
  name: 'Login',
  data: () => {
    return {
      is_hidden: false,
      is_alert: false,
      alert_title: "",
      alert_content: "",
      username: "",
      gamecode: "",
    };
  },
  created() {
    this.init();
  },
  methods: {
    init: async function() {
      localStorage.clear(); // 저장소 데이터 전체 삭제
    },
    /**
     * 로그인 처리를 수행한다.
     *
     * 1. 입력된 사용자 이름의 길이를 확인한다.
     * 1.1. 입력된 값이 없다면, 메시지를 출력한다.
     * 2. 기 등록된 사용자 여부를 점검한다.
     * 2.1. 등록되지 않은 경우, 사용자를 생성한다.
     * 3. 해당 사용자 정보를 로컬 스토리지에 저장 후, 로그인 처리를 수행한다.
     * 3.1. Game 입장 Code가 있는 경우,
     * 3.1.1. 해당 Game이 존재하는 경우, 해당 게임에 입장한다.
     * 3.1.2. 해당 Game이 존재하지 않는 경우, 로그인 처리를 수행한다.
     */
    login: async function() {
      // 1. 입력된 사용자 이름의 길이를 확인한다.
      if (this.username.length < 1) {
        // 1.1. 입력된 값이 없다면, 메시지를 출력한다.
        this.$dialog.alert_dialog("로그인 실패", "사용자 이름을 입력해 주세요.");
      } else {
        let response;

        try {
          // 2. 기 등록된 사용자 여부를 점검한다.
          response = await user_api.isuser(this.username);
        } catch (err) {
          if (err.response.data.error_code == 404) {
            // 2.1. 등록되지 않은 경우, 사용자를 생성한다.
            response = await user_api.login(this.username);
          } else {
            this.$dialog.alert_dialog("시스템 에러", "예기치 못한 에러가 발생했습니다.");
          } 
        }
        // 3. 해당 사용자 정보를 로컬 스토리지에 저정 후, 로그인 처리를 수행한다.
        localStorage.setItem("in2game.user", JSON.stringify(response.data));
        
        if(this.$route.query.gamecode === undefined) {
          this.$router.push({ path: 'lobby' });
        } else {
          // 3.1. Game 입장 Code가 있는 경우,
          try {
            response = await game_api.isgame(JSON.parse('{ "gamecode" : "' + this.$route.query.gamecode + '"}'));
            if (response.data.state == 0) {
              // 3.1.1. 해당 Game이 존재하는 경우, 해당 게임에 입장한다.
              this.join_game(response.data);
            } else {
              this.$dialog.alert_dialog("시스템 에러", "예기치 못한 에러가 발생했습니다.");
            }  
            // 3.1.1. 해당 Game이 존재하는 경우, 해당 게임에 입장한다.
            this.join_game(response.data);
          } catch (err) {
            if (err.response.data.error_code == 404) {
              // 3.1.2. 해당 Game이 존재하지 않는 경우, 로그인 처리를 수행한다.
              this.$router.push({ path: 'lobby' });
            } else {
              this.$dialog.alert_dialog("시스템 에러", "예기치 못한 에러가 발생했습니다.");
            } 
          }
        }
      }
    },
    /**
     * 사용자를 게임 플레이어로 추가한다.
     *
     * @param : gamecode 게임코드
     * 1. 해당 게임의 플레이어 여부를 확인한다.
     * 1.1. 기존 플레이어가 아닌 경우, 참가 가능 인원을 확인한다.
     * 1.1.1. 참가 가능한 경우, 플레이어 추가한다.
     * 1.1.2. 생성된 게임 정보를 로컬 스토리지에 저장 후, 게임으로 이동한다.
     * 1.1.3. 게임의 참가인원이 초과된 경우, 메시지를 출력한다.
     * 1.2. 기존 플레이어인 경우, 게임 정보를 로컬 스토리지에 저장 후, 게임으로 이동한다.
     * 1.3. 해당 플레이어 정보가 여러개인 경우, 시스템 오류
     */
    join_game: async function(game) {
      let response;

      // 1. 해당 게임의 플레이어 여부를 확인한다.
      response = await gamer_api.isgamer(game, JSON.parse(localStorage.getItem("in2game.user")));

      if (response.data.length == 0) {
        // 1.1.1. 참가 가능한 경우, 플레이어 추가한다.
        response = await gamer_api.joingame(game, JSON.parse(localStorage.getItem("in2game.user")));

        if (response.status == 201 || response.status == 208) {
          // 1.1.2. 생성된 게임 정보를 로컬 스토리지에 저장 후, 게임으로 이동한다.
          localStorage.setItem("in2game.game", JSON.stringify(game));
          this.$router.push({ path: 'game' });
        } else {
          this.$dialog.alert_dialog("시스템 에러", "예기치 못한 에러가 발생했습니다.");
        }  
      } else if (response.data.length == 1) {
        // 1.2. 기존 플레이어인 경우, 게임 정보를 로컬 스토리지에 저장 후, 게임으로 이동한다.
        localStorage.setItem("in2game.game", JSON.stringify(game));
        this.$router.push({ path: 'game' });
      } else {
        // 1.3. 해당 플레이어 정보가 여러개인 경우, 시스템 오류
        this.$dialog.alert_dialog("시스템 에러", "예기치 못한 에러가 발생했습니다.");
      }
    },
  },
};
</script>