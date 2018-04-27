<template lang="pug">
.flashed-messages
  b-container(
    v-if="messages.length"
  )
    b-row(v-for="message, id in messages" :key="'msg' + id")
      b-col(md="12")
        b-alert(
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
  mounted () {
    this.$store.dispatch('flash/load')
  }
}
</script>

<style>
.flashed-messages {
  padding-top: 1rem;
  width: 100%;
}
</style>
