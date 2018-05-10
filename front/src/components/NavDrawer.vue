<template lang="pug">
v-navigation-drawer(
  persistent
  :mini-variant="miniVariant"
  :clipped="clipped"
  v-model="drawer"
  enable-resize-watcher
  fixed
  app
)
  v-list
    template(v-if="isAuthenticated")
      template(v-for="(link, id) in userLinks")
        template(v-if="!link.admin || user.is_admin")
          b-nav-item-dropdown(
            right
            v-if="link.items"
            :key="id"
          )
            template(slot="button-content") {{ link.title }}
            b-dropdown-item(
              v-for="(item, itemId) in link.items"
              :key="itemId"
              :to="item.to"
            ) {{item.title}}

          v-list-tile(
            v-else
            value="true"
            :key="id"
            :to="link.to"
          )
            v-list-tile-action
              v-icon(v-html="link.icon")
            v-list-tile-content
              v-list-tile-title(v-text="link.title")

          v-list-tile(
            v-else
            value="true"
            :key="id"
            :to="link.to"
          )
            v-list-tile-action
              v-icon user
              v-list-tile-content
                v-list-tile-title Hi, {{ user.username }}!

    template(v-else)
      template(v-for="(link, id) in guestLinks")
        v-list-tile(
          value="true"
          :key="id"
          :to="link.to"
        )
          v-list-tile-action
            v-icon(v-html="link.icon")
          v-list-tile-content
            v-list-tile-title(v-text="link.title")
</template>

<script>
export default {
  name: 'app-header',
  computed: {
    user () { return this.$store.getters['user/user'] },
    isAuthenticated () { return this.$store.getters['user/isAuthenticated'] },

    state () { return this.$store.state.menu.navDrawer },

    miniVariant () { return this.$store.state.menu.miniVariant },
    clipped () { return this.$store.state.menu.clipped }
  },
  data () {
    return {
      drawer: this.state,

      userLinks: [
        { title: 'Dashboard', icon: 'web', to: '/' },
        { title: 'RPG', to: '/rpg/index' },
        {
          title: 'Systems',
          items: [
            { title: 'Pathfinder', to: '/pathfinder/index' },
            { title: 'GURPS', to: '/gurps/index' },
            { title: 'Tunels & Trolls', to: '/tnt/index' }
          ]
        },
        { title: 'Worlds', to: '/worlds/list' },
        {
          admin: true,
          title: 'Admin',
          items: [
            { title: 'Departments', to: '/admin/list_departments' },
            { title: 'Roles', to: '/admin/list_roles' },
            { title: 'Employees', to: '/admin/list_employees' }
          ]
        },
        { title: 'Logout', to: '/auth/logout' }
      ],
      guestLinks: [
        { title: 'Home', icon: 'home', to: '/' },
        { title: 'Register', icon: 'person_add', to: '/auth/register' },
        { title: 'Login', icon: 'person', to: '/auth/login' }
      ]
    }
  },
  watch: {
    drawer (value) {
      this.$store.commit('setNavDrawer', value)
    },
    state (value) {
      this.drawer = value
    }
  }
}
</script>

<style scoped lang="scss">
.navigation-drawer {
  opacity: 0.90;
}
</style>
