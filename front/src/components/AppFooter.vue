<template lang="pug">
v-footer(:fixed="fixed" app)
  v-layout(row wrap justify-center)
    v-btn(flat small color="primary" to="/") Home
    template(v-if="isAuthenticated")
      v-btn(flat small color="primary" to="/auth/logout") Logout
    template(v-else)
      v-btn(flat small color="primary" to="/auth/register") Register
      v-btn(flat small color="primary" to="/auth/login") Login
    v-flex(xs12 pd-3 text-xs-center class="caption copyright grey--text text--darken-1")
      | Copyright {{user}} ({{ token }}) &copy; {{year}}/ All Rights Reserved
</template>

<script>
export default {
  name: 'app-footer',
  computed: {
    fixed () { return this.$store.state.menu.fixed },
    token () { return this.$store.state.user.token },
    user () { return this.$store.getters['user/user'] },
    isAuthenticated () { return this.$store.getters['user/isAuthenticated'] }
  },
  data: () => ({
    year: 2018
  })
}
</script>

<style scoped lang="scss">
@import "./scss/_colors.scss";

footer {
  padding: 50px 0;
  background-color: $footerColor;
}

footer .nav .nav-link, footer .nav .footer-menu-divider {
  padding: 0px 5px;
}
</style>
