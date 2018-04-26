<template lang="pug">
#app
  header
    // nav(class="navbar navbar-inverse navbar-fixed-top")
    // nav(class="navbar navbar-default navbar-fixed-top topnav" role="navigation")
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
            template(v-if="current_user.is_authenticated")
              b-nav-item(:to="current_user.after_login") Dashboard
              b-nav-item(to="/rpg/index") RPG
              b-nav-item-dropdown(right)
                template(slot="button-content") Systems
                b-dropdown-item(to="/pathfinder/index") Pathfinder
                b-dropdown-item(to="/gurps/index") GURPS
                b-dropdown-item(to="/tnt/index") Tunnels & Trolls
              b-nav-item(to="/world/world_list") Worlds
              b-nav-item-dropdown(right v-if="current_user.is_admin")
                template(slot="button-content") Admin
                b-dropdown-item(to="/admin/list_departments") Departments
                b-dropdown-item(to="/admin/list_roles") Roles
                b-dropdown-item(to="/admin/list_eployees") Employees
              b-nav-item(to="/auth/logout") Logout
              b-nav-item <i class="fa fa-user"></i> Hi, {{ current_user.username }}!
            template(v-else)
              b-nav-item(to="/home/index") Home
              b-nav-item(to="/auth/register") Register
              b-nav-item(to="/auth/login") Login

  b-container
    #confirm-del(class="modal fade", tabindex=-1, role="dialog")
      .modal-dialog
        .modal-content
          .modal-header Вы уверены?
          .modal-body ...
          .modal-footer
            button(type="button", class="btn btn-default", data-dismiss="modal") Отменить
            a(class="btn btn-default btn-danger btn-ok") Удалить

    b-alert(
      v-for="message, id in messages"
      :key="id"
      :variant="message.category"
      show
    ) message.message

    div(class="row wrapper")
      // include _panel.pug
      router-view
    .push

  footer
    b-container
      b-row
        b-col(col lg="12")
          b-nav
            b-nav-item(to="/home/homepage") Home
            li.footer-menu-divider .
            template(v-if="current_user.is_authenticated")
              b-nav-item(to="/auth/logout") Logout
            template(v-else)
              b-nav-item(to="/auth/register") Register
              li.footer-menu-divider .
              b-nav-item(to="/auth/login") Login
          p(class="copyright text-muted small") Copyright &copy; 2017/ All Rights Reserved
</template>

<script>
export default {
  data () {
    // {% with messages = get_flashed_messages(with_categories=True) %}
    return {
      appname: 'RPG-Helper',
      current_user: {
        is_authenticated: false
      },
      messages: [
        // { category: 'info', message: 'text' },
        // { category: 'info', message: 'text' },
        // { category: 'info', message: 'text' }
      ]
    }
  },
  name: 'app'
}
</script>

<style lang="scss">
#app {
  // font-family: 'Avenir', Helvetica, Arial, sans-serif;
  // -webkit-font-smoothing: antialiased;
  // -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  // color: #2c3e50;
  // margin-top: 60px;
}

@import "./scss/_navbar.scss";
@import "./scss/style.scss";
@import "./scss/_theme.scss";
</style>

<style scoped lang="scss">
.navbar-light {
  background-color: #f8f8f8;
  border-bottom: solid 1px #e7e7e7;
}

.navbar-light .navbar-nav .nav-link {
  color: #aec251;
}

.navbar-light .navbar-nav .nav-link:hover {
  color: #687430;
}

footer .nav .nav-link, footer .nav .footer-menu-divider {
  padding: 0px 5px;
}
</style>
