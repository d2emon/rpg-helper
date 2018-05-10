<template lang="pug">
v-toolbar(
  app
  :clipped-left="clipped"
)
  v-toolbar-side-icon('@click.stop'="switchNavDrawer")
  v-btn(icon '@click.stop'="switchMini")
    v-icon(v-html="miniVariant ? 'chevron_right' : 'chevron_left'")
  v-toolbar-title(v-text="appname")
  v-spacer
  v-btn(icon '@click.stop'="switchUtilityDrawer")
    v-icon menu
</template>

<script>
export default {
  name: 'app-header',
  computed: {
    // drawer () { return this.$store.state.menu.drawer },
    miniVariant () { return this.$store.state.menu.miniVariant },
    clipped () { return this.$store.state.menu.clipped }
    // fixed () { return this.$store.state.menu.fixed },
  },
  data () {
    return {
      appname: 'RPG-Helper'
    }
  },
  methods: {
    switchMini () {
      this.$store.commit('switchMini')
    },
    switchNavDrawer () {
      this.$store.commit('switchNavDrawer')
    },
    switchUtilityDrawer () {
      this.$store.commit('switchUtilityDrawer')
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
