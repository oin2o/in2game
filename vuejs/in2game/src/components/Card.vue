<template>
    <v-card color="#385F73" dark>
        <v-card-title class="text-h5">
            Unlimited music now
        </v-card-title>
        <v-card-subtitle>{{ card.gamename }}</v-card-subtitle>
        <v-card-actions>
            <v-btn text>
            Listen Now
            </v-btn>
        </v-card-actions>
    </v-card>
</template>
<script>
export default {
  name: 'Card',
  props: {
    card: Object,
  },
  data: () => {
    return {
    };
  },
};
</script>