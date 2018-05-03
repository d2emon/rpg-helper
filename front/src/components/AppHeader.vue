<template lang="pug">
header
  b-navbar(
    toggleable="md"
    fixed="top"
    class="topnav"
    type="light"
    variant="light"
  )
    b-container
      b-navbar-toggle(target="nav_collapse")
      b-navbar-brand(
        to="/"
        class="topnav"
        v-text="appname"
      )
      b-collapse(is-nav id="nav_collapse")
        b-navbar-nav(class="ml-auto")
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
                b-nav-item(
                  v-else
                  :key="id"
                  :to="link.to"
                ) {{link.title}}
            b-nav-item <i class="fa fa-user"></i> Hi, {{ user.username }}!

          template(v-else)
            template(v-for="(link, id) in guestLinks")
              b-nav-item(
                :key="id"
                :to="link.to"
              ) {{ link.title }}
</template>

<script>
export default {
  name: 'app-header',
  computed: {
    user () { return this.$store.getters['user/user'] },
    isAuthenticated () { return this.$store.getters['user/isAuthenticated'] }
  },
  data () {
    return {
      appname: 'RPG-Helper',

      userLinks: [
        { title: 'Dashboard', to: '/' },
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
        { title: 'Home', to: '/' },
        { title: 'Register', to: '/auth/register' },
        { title: 'Login', to: '/auth/login' }
      ]
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
