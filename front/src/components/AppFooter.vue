<template lang="pug">
footer
  b-container
    b-row
      b-col(col lg="12")
        b-nav
          b-nav-item(to="/") Home
          li.footer-menu-divider .
          template(v-if="current_user.is_authenticated")
            b-nav-item(to="/auth/logout") Logout
          template(v-else)
            b-nav-item(to="/auth/register") Register
            li.footer-menu-divider .
            b-nav-item(to="/auth/login") Login
        p(class="copyright text-muted small") Copyright &copy; {{year}}/ All Rights Reserved
</template>

<script>
var currentUser = {
  username: 'Username',
  is_authenticated: false,
  is_admin: true,
  after_login: '/'
}

export default {
  name: 'app-footer',
  data: () => ({
    current_user: currentUser,
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
