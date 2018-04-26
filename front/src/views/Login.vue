<template lang="pug">
.content-section
  br

  b-container(
    v-if="utils.flashed_messages.length"
    class="flashed-messages"
  )
    b-row(v-for="message, id in utils.flashed_messages")
      b-col(md="12")
        b-alert(
          :key="id"
          :variant="message.category"
          show
        ) {{ message.message }}

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
export default {
  name: 'login',
  data () {
    // {% import "bootstrap/utils.html" as utils %}
    // {% import "bootstrap/wtf.html" as wtf %}
    return {
      appname: 'Login',
      msg: 'Login to your account',
      utils: {
        flashed_messages: [
          // { category: 'info', message: 'Invalid email or password' }
        ]
      },
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h1 {
  font-size: 36px;
}

.content-section {
  padding-top: 100px;
  width: 100%;
}

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
