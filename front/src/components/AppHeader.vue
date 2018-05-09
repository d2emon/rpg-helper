<template lang="pug">
v-toolbar(
  app
  :clipped-left="clipped"
)
  v-toolbar-side-icon('@click.stop'="drawer = !drawer")
  v-btn(icon '@click.stop'="miniVariant = !miniVariant")
    v-icon(v-html="miniVariant ? 'chevron_right' : 'chevron_left'")
  v-btn(icon '@click.stop'="clipped = !clipped")
    v-icon web
  v-btn(icon '@click.stop'="fixed = !fixed")
    v-icon remove
  v-toolbar-title(v-text="appname")
  v-spacer
  v-btn(icon '@click.stop'="rightDrawer = !rightDrawer")
    v-icon menu
</template>

<script>
export default {
  name: 'app-header',
  data () {
    return {
      appname: 'RPG-Helper',

      clipped: false,
      drawer: null,
      miniVariant: true,
      rightDrawer: true
    }
  }
}
</script>

<style scoped lang="scss">
header {
  font-size: 14px;
}

.navbar-light {
  background-color: #f8f8f8;
  border-bottom: solid 1px #e7e7e7;
}
</style>

<style lang="scss">
.navbar-light .navbar-nav .nav-link {
  color: #aec251 !important;
}

.navbar-light .navbar-nav .nav-link:hover {
  color: #687430 !important;
}
</style>
