<template>
  <v-dialog v-model="is_show">
    <v-overlay>
        <v-card>
          <v-card-title class="text-h6">{{ title }}</v-card-title>
          <v-card-text>{{ message }}</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary darken-1" text @click="$emit('close_dialog')">확인</v-btn>
          </v-card-actions>
        </v-card>
    </v-overlay>
  </v-dialog>
</template>
<script>
export default {
  name: 'Dialog',
  props: {
    is_show: Boolean,
    title: String,
    message: String,
  },
}
</script>