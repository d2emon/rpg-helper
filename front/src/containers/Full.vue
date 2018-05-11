<template lang="pug">
v-app
  nav-drawer

  app-header
  v-content
    // confirm-del
    // messages
    div(class="row wrapper")
      flashed-messages

      // include _panel.pug
      router-view
    .push
    utility-drawer

  app-footer
</template>

<script>
import {
  NavDrawer,
  UtilityDrawer,
  AppHeader,
  AppFooter,
  ConfirmDel,
  Messages,
  FlashedMessages
} from '@/components/'

export default {
  components: {
    NavDrawer,
    UtilityDrawer,
    AppHeader,
    AppFooter,
    ConfirmDel,
    Messages,
    FlashedMessages
  },
  name: 'full'
}
</script>

<style scoped>
.wrapper {
  // position: absolute;
  // left: 0px;
  // width: 100%;
}
</style>
