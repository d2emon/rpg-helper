<template lang="pug">
.flashed-messages
  v-container(
    v-if="messages.length"
    class="my-3"
  )
    template(
      v-for="message, id in messages"
    )
      v-alert(
        :key="'msg_' + id"
        :type="message.category"
        :value="true"
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
        category: 'error',
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
.flashed-messages.container {
  padding-top: 1rem;
  width: 100%;
}
</style>
