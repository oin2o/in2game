<template>
  <v-main>
    <v-dialog v-model="cre8_game" persistent>
      <v-card>
        <v-card-title>
          <span class="text-h6">게임 만들기</span>
        </v-card-title>
        <v-card-text>
          <v-select v-model="game_name" :items="game_names" item-text="value" item-value="key" prepend-icon="mdi-gamepad-variant" append-icon="" dense solo flat readonly></v-select>
          <v-select v-model="game_name" :items="number_gamers" item-text="value" item-value="key" prepend-icon="mdi-human-queue" append-icon="" dense solo flat readonly></v-select>
          <v-select v-model="game_name" :items="game_types" item-text="value" item-value="key" prepend-icon="mdi-tag-multiple" append-icon="" dense solo flat readonly></v-select>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="orange darken-1" text @click="$emit('close_dialog')">취소</v-btn>
          <v-btn color="primary darken-1" text @click="$emit('create_game')">만들기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="overcrowding" persistent>
      <v-card>
        <v-card-title class="text-h6">게임 참가 실패</v-card-title>
        <v-card-text>더이상 참가할 수 없습니다.(최대 {{ max_gamers[game_name] }}명)</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" text @click="$emit('close_dialog')">확인</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="biz_error" persistent>
      <v-card>
        <v-card-title class="text-h6">게임 만들기 실패</v-card-title>
        <v-card-text>일시적인 에러가 발생했습니다.<br>에러가 계속되는 경우, 관리자에게 문의해 주세요.</v-card-text>
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
    biz_error: Boolean,
    cre8_game: Boolean,
    overcrowding: Boolean,
    sys_error: Boolean,
    game_name: String,
  },
  data: () => {
    return {
      game_names: [
        { key: 'dalmuti', value: '달무티'},{ key: 'dixit', value: '딕싯'},
        { key: 'davinci', value: '다빈치코드'},{ key: 'liar', value: '라이어게임'}
      ],
      number_gamers: [
        { key: 'dalmuti', value: '5인 ~ 8인'},{ key: 'dixit', value: '4인 ~ 8인'},
        { key: 'davinci', value: '2인 ~ 4인'},{ key: 'liar', value: '4인 ~ 8인'}
      ],
      game_types: [
        { key: 'dalmuti', value: '핸드관리/클라이밍'},{ key: 'dixit', value: '스토리텔링'},
        { key: 'davinci', value: '추리'},{ key: 'liar', value: '블러핑'}
      ],
      max_gamers: { 'dalmuti': 8, 'dixit': 8, 'davinci': 4, 'liar': 8},
    };
  },
};
</script>
