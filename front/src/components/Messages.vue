<template lang="pug">
div
  b-alert(
    v-for="message, id in messages"
    :key="id"
    :variant="message.category"
    show
  ) message.message
</template>

<script>
export default {
  name: 'messages',
  data () {
    // {% with messages = get_flashed_messages(with_categories=True) %}
    return {
      messages: []
    }
  }
}
</script>
