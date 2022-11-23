<template>
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
</template>
<script>
export default {
  name: 'LobbyDialog',
  props: {
    cre8_game: Boolean,
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
    };
  },
};
</script>
