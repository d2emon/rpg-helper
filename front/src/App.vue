<template lang="pug">
#app
  app-header
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

  app-footer
</template>

<script>
import {
  AppHeader,
  AppFooter,
  ConfirmDel,
  Messages
} from '@/components/'

export default {
  components: {
    AppHeader,
    AppFooter,
    ConfirmDel,
    Messages
  },
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

<style>
/* Import Font Awesome Icons Set */
$fa-font-path: '~font-awesome/fonts/';
@import '~font-awesome/css/font-awesome.min.css';
</style>

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
