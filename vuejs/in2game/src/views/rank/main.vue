<template>
  <v-main id="rankBack" class="overflow-y-auto">
    <MenuSection v-bind:is_chat=false v-bind:menu_name=menu_name @call_back_menu="call_back_menu" />
    <v-container id="scrolling-app-bar" class="fill-height overflow-y-auto" fluid>
    </v-container>
  </v-main>
</template>
<script>
import MenuSection from '@/components/Menu';

export default {
  name: 'Rank',
  components: {
    MenuSection,
  },
  data: () => {
    return {
      is_chat: false,
      menu_name: "all",
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
     */
    init: async function() {
      // 1. 로컬 스토리지의 사용자 정보 여부를 확인한다.
      if (!localStorage.getItem("in2game.user")) {
        // 1.1. 사용자 정보가 없는 경우, 로그인 페이지로 이동한다.
        this.$router.push({ path: '/' });
      }
    },
    call_back_menu: function(game_name) {
    },
  },
};
</script>