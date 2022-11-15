<template>
  <v-main id="loginBack" class="overflow-y-auto">
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
    <DialogSection v-bind:chk_username=chk_username v-bind:sys_error=sys_error @close_dialog="close_dialog" />
  </v-main>
</template>
<script>
import user_api from '@/api/user';
import DialogSection from './components/dialog';

export default {
  name: 'Login',
  components: {
    DialogSection,
  },
  data: () => {
    return {
      chk_username: false,
      is_hidden: false,
      sys_error: false,
      username: "",
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
     * 3. 해당 사용자 정보를 로컬 스토리지에 저정 후, 로그인 처리를 수행한다.
     */
    login: async function() {
      // 1. 입력된 사용자 이름의 길이를 확인한다.
      if (this.username.length < 1) {
        // 1.1. 입력된 값이 없다면, 메시지를 출력한다.
        this.chk_username = true;
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
            this.sys_error = true;
          } 
        }
        // 3. 해당 사용자 정보를 로컬 스토리지에 저정 후, 로그인 처리를 수행한다.
        localStorage.setItem("in2game.user", JSON.stringify(response.data));
        this.$router.push({ path: 'lobby' });
      }
    },
    close_dialog: function(){
      this.chk_username = false;
      this.sys_error = false;
    },
  },
};
</script>