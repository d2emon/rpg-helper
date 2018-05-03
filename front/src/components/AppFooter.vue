<template lang="pug">
footer
  b-container
    b-row
      b-col(col lg="12")
        b-nav
          b-nav-item(to="/") Home
          li.footer-menu-divider .
          template(v-if="isAuthenticated")
            b-nav-item(to="/auth/logout") Logout
          template(v-else)
            b-nav-item(to="/auth/register") Register
            li.footer-menu-divider .
            b-nav-item(to="/auth/login") Login
        p(class="copyright text-muted small") Copyright {{user}} ({{ token }}) &copy; {{year}}/ All Rights Reserved
</template>

<script>
export default {
  name: 'app-footer',
  computed: {
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
