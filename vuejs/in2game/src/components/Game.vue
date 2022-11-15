<template>
    <v-card>
      <v-img v-bind:src="require(`@/assets/images/cards/${game.gamename}/${game.chapter%14}.png`)" class="white--text align-end" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)" @click="$emit('join_game', game)" >
        <v-card-title class="justify-center pa-0" v-bind:style="{ fontSize: 0.8 + 'rem' }" v-text="game.gamecode"></v-card-title>
      </v-img>
    </v-card>
</template>
<script>
export default {
  name: 'Card',
  props: {
    game: Object,
  },
  data: () => {
    return {
    };
  },
};
</script>