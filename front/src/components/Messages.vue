<template lang="pug">
div
  b-alert(
    v-for="message, id in messages"
    :key="id"
    :variant="message.category"
    show
  ) {{ message.message }}
</template>

<script>
export default {
  name: 'messages',
  computed: {
    messages () { return this.$store.state.flash.messages }
  },
  update () {
    this.$store.dispatch('flash/load')
  }
}
</script>
