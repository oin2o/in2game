<template>
  <v-main>
    <v-dialog v-model="chk_username" persistent>
      <v-card>
        <v-card-title class="text-h6">로그인 실패</v-card-title>
        <v-card-text>사용자 이름을 입력해 주세요.</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" text @click="$emit('close_dialog')">확인</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="sys_error" persistent>
      <v-card>
        <v-card-title class="text-h6">시스템 에러</v-card-title>
        <v-card-text>예기치 못한 에러가 발생했습니다.<br>관리자에게 문의해 주세요.</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" text @click="$emit('close_dialog')">확인</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-main>
</template>
<script>
export default {
  name: 'Dialog',
  props: {
    chk_username: Boolean,
    sys_error: Boolean,
  },
  data: () => {
    return {
    };
  },
};
</script>
