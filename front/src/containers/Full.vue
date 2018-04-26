<template lang="pug">
#app
  app-header
  b-container
    confirm-del
    messages

    div(class="row wrapper")
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
  Messages
} from '@/components/'

export default {
  components: {
    AppHeader,
    AppFooter,
    ConfirmDel,
    Messages
  },
  name: 'full'
}
</script>
