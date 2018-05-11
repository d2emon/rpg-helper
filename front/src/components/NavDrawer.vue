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
          v-list-group(
            v-if="link.items"
            v-model="link.model"
            :key="id"
            :append-icon="link.model ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
            :prepend-icon="link.icon"
          )
            v-list-tile(slot="activator")
              v-list-tile-content
                v-list-tile-title {{ link.title }}
            v-list-tile(
              v-for="(item, itemId) in link.items"
              :key="id + '-' + itemId"
              :to="item.to"
            )
              v-list-tile-action(v-if="item.icon")
                v-icon(v-html="item.icon")
              v-list-tile-content
                v-list-tile-title(v-text="item.title")
          v-list-tile(
            v-else
            value="true"
            :key="id"
            :to="link.to"
          )
            v-list-tile-action(v-if="link.icon")
              v-icon(v-html="link.icon")
            v-list-tile-content
              v-list-tile-title(v-text="link.title")
      v-list-tile(
        value="true"
      )
        v-list-tile-action
          v-icon person
        v-list-tile-content
          v-list-tile-title Hi, {{ user.username }}!
    template(v-else)
      template(v-for="(link, id) in guestLinks")
        v-list-tile(
          value="true"
          :key="id"
          :to="link.to"
        )
          v-list-tile-action(v-if="link.icon")
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
        { title: 'RPG', icon: 'casino', to: '/rpg/index' },
        {
          title: 'Systems',
          icon: 'pages',
          items: [
            { title: 'Pathfinder', icon: 'business_center', to: '/pathfinder/index' },
            { title: 'GURPS', icon: 'business_center', to: '/gurps/index' },
            { title: 'Tunnels & Trolls', icon: 'business_center', to: '/tnt/index' }
          ]
        },
        { title: 'Worlds', icon: 'public', to: '/worlds/list' },
        {
          admin: true,
          title: 'Admin',
          icon: 'supervisor_account',
          items: [
            { title: 'Departments', icon: 'business', to: '/admin/list_departments' },
            { title: 'Roles', icon: 'business', to: '/admin/list_roles' },
            { title: 'Employees', icon: 'business', to: '/admin/list_employees' }
          ]
        },
        { title: 'Logout', icon: 'exit_to_app', to: '/auth/logout' }
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
