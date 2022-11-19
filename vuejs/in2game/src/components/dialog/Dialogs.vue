<template>
  <DialogSection v-bind:is_show=is_show v-bind:title=title v-bind:message=message @close_dialog="close_dialog" />
</template>
<script>
import DialogSection from './Dialog'

export default {
  name: 'Dialogs',
  components: { 
    DialogSection,
  },
  data() {
    return {
      is_show: false,
      title: "",
      message: "",
    }
  },
  methods: {
    open_dialog() {
      if (!this.$parent) {
        this.$mount();
        document.body.appendChild(this.$el);
      }
    },
    alert_dialog(title, message, type) {
      this.is_show = true;
      this.title = title;
      this.message = message;

      this.open_dialog();
    },
    close_dialog() {
      this.is_show = false;
    },
  },
}
</script>