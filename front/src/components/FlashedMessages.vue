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
import { MessageBus } from '@/store/messages'

export default {
  name: 'messages',
  computed: {
    messages () { return this.$store.state.flash.messages }
  },
  mounted () {
    // this.$store.dispatch('flash/load')

    MessageBus.$on('newMessage', msg => {
      console.log('Message ', msg)
      this.$store.commit('flash/addMessage', {
        category: 'info',
        message: msg
      })
    })
    MessageBus.$on('newError', msg => {
      console.error(msg)
      this.$store.commit('flash/addMessage', {
        category: 'danger',
        message: msg
      })
    })
  },
  beforeDestroy () {
    MessageBus.$off('newMessage')
    MessageBus.$off('newError')
  }
}
</script>

<style>
.flashed-messages {
  padding-top: 1rem;
  width: 100%;
}
</style>
