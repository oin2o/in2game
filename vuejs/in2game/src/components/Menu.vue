<template>
  <v-app-bar id="fixed-tool-bar" dense hide-on-scroll scroll-target="#scrolling-app-bar" elevation="0">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn icon>
          <v-icon id="shadow-text" large color="orange accent-3" v-bind="attrs" v-on="on">mdi-gamepad-variant</v-icon>
        </v-btn>
      </template>
      <v-list dense>
        <v-list-item>
          <v-list-item-icon>
            <v-icon id="shadow-text">mdi-face-recognition</v-icon>
          </v-list-item-icon>
          <v-list-item-title id="bold-shadow-text">{{ user.username }}</v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item v-for="(menu, i) in menus" :key="i" :to="menu.link" link>
          <v-list-item-icon>
            <v-icon id="shadow-text">mdi-{{ menu.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title id="shadow-text">{{ menu.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-btn v-if="is_chat" icon>
      <v-icon id="shadow-text" large color="white accent-3">mdi-forum-outline</v-icon>
    </v-btn>
    <v-spacer></v-spacer>
    <v-btn v-if="menu_name == 'all' || menu_name == 'dalmuti'" @click="$emit('call_back_menu', 'dalmuti')" icon>
      <v-avatar size="36">
        <v-img src="~@/assets/images/cards/dalmuti/icon.png"></v-img>
      </v-avatar>
    </v-btn>
    <!--
    <v-btn v-if="menu_name == 'all' || menu_name == 'dixit'" @click="$emit('call_back_menu', 'dixit')" icon>
      <v-avatar size="36">
        <v-img src="~@/assets/images/cards/dixit/icon.png"></v-img>
      </v-avatar>
    </v-btn>
    <v-btn v-if="menu_name == 'all' || menu_name == 'davinci'" @click="$emit('call_back_menu', 'davinci')" icon>
      <v-avatar size="36">
        <v-img src="~@/assets/images/cards/davinci/icon.png"></v-img>
      </v-avatar>
    </v-btn>
    <v-btn v-if="menu_name == 'all' || menu_name == 'liar'" @click="$emit('call_back_menu', 'liar')" icon>
      <v-avatar size="36">
        <v-img src="~@/assets/images/cards/liar/icon.png"></v-img>
      </v-avatar>
    </v-btn>
    -->
  </v-app-bar>
</template>
<script>
export default {
  name: 'Menu',
  props: {
    is_chat: Boolean,
    menu_name: String,
  },
  data: () => {
    return {
      user: JSON.parse(localStorage.getItem("in2game.user")),
      menus: [
        { icon:'nintendo-switch', title:'게임시작', link:'/lobby' },
        { icon:'book-open-variant', title:'설명', link:'/explain' },
        { icon:'trophy-outline', title:'전적', link:'/rank' },
        { icon:'logout', title:'나가기', link:'/' },
      ],
    };
  },
};
</script>
