<template lang="pug">
v-navigation-drawer(
  temporary
  :right="right"
  v-model="drawer"
  fixed
  app
)
  v-list
    v-list-tile('@click'="right = !right")
      v-list-tile-action
        v-icon compare_arrows
      v-list-tile-title Switch drawer (click me)
</template>

<script>
export default {
  name: 'utility-drawer',
  computed: {
    state () { return this.$store.state.menu.utilityDrawer }
  },
  data () {
    return {
      right: true,
      drawer: this.state
    }
  },
  watch: {
    drawer (value) {
      this.$store.commit('setUtilityDrawer', value)
    },
    state (value) {
      this.drawer = value
    }
  }
}
</script>
