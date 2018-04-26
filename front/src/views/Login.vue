<template lang="pug">
.container(class="content-section")
  br

  flashed-messages

  br
  .center
    h1 {{ msg }}
    br
    b-form(@submit="onSubmit")
      b-form-group(
        id="usernameInputGroup"
        label="Username:"
        label-for="usernameInput"
      )
        b-form-input(
          id="usernameInput"
          v-model="form.username"
          required
        )
      b-form-group(
        id="passwordInputGroup"
        label="Password:"
        label-for="passwordInput"
      )
        b-form-input(
          id="passwordInput"
          type="password"
          v-model="form.password"
          required
        )
      b-button(type="submit" variant="outline-primary") Login
</template>

<script>
import {
  FlashedMessages
} from '@/components/'

export default {
  name: 'login',
  components: {
    FlashedMessages
  },
  data () {
    // {% import "bootstrap/utils.html" as utils %}
    // {% import "bootstrap/wtf.html" as wtf %}
    return {
      msg: 'Login to your account',
      form: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    onSubmit () {
      alert(this.form)
    }
  }
}
</script>

<style scoped lang="scss">
@import "./scss/_colors.scss";

.btn-outline-primary {
    border-color: $btnBorder;
    color: $btnColor;
}

.btn-outline-primary:hover {
    background-color: $btnHover;
    color: #000000;
}
</style>
