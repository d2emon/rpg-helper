<template lang="pug">
v-app
  nav-drawer

  app-header
  v-content
    // confirm-del
    // messages
    div(class="row wrapper")
      // flashed-messages

      // include _panel.pug
      router-view
    .push
  v-navigation-drawer(
    temporary
    :right="right"
    v-model="rightDrawer"
    fixed
    app
  )
    v-list
      v-list-tile('@click'="right = !right")
        v-list-tile-action
          v-icon compare_arrows
        v-list-tile-title Switch drawer (click me)

  app-footer
</template>

<script>
import {
  NavDrawer,
  AppHeader,
  AppFooter,
  ConfirmDel,
  Messages,
  FlashedMessages
} from '@/components/'

export default {
  components: {
    NavDrawer,
    AppHeader,
    AppFooter,
    ConfirmDel,
    Messages,
    FlashedMessages
  },
  data () {
    return {
      right: true,
      rightDrawer: false
    }
  },
  name: 'full'
}
</script>

<style>
#app {
  padding-top: 50px;
}
</style>
