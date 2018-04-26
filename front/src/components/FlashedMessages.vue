<template lang="pug">
div
  b-container(
    v-if="utils.flashed_messages.length"
    class="flashed-messages"
  )
    b-row(v-for="message, id in utils.flashed_messages")
      b-col(md="12" :key="id")
        b-alert(
          :variant="message.category"
          show
        ) {{ message.message }}

</template>

<script>
export default {
  name: 'messages',
  data () {
    // {% with messages = get_flashed_messages(with_categories=True) %}
    return {
      utils: {
        flashed_messages: [
          // { category: 'info', message: 'Invalid email or password' }
        ]
      }
    }
  }
}
</script>
