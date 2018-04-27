<template lang="pug">
#app
  app-header
  b-container
    // confirm-del
    // messages
    div(class="row wrapper")
      // flashed-messages

      // include _panel.pug
      router-view
    .push

  app-footer
</template>

<script>
import {
  AppHeader,
  AppFooter,
  ConfirmDel,
  Messages,
  FlashedMessages
} from '@/components/'

export default {
  components: {
    AppHeader,
    AppFooter,
    ConfirmDel,
    Messages,
    FlashedMessages
  },
  name: 'full'
}
</script>

<style>
#app {
  padding-top: 50px;
}
</style>
