<template lang="pug">
.container(class="content-section")
  br

  flashed-messages

  br
  .center
    h1 {{ msg }}
    br
    v-form(
      ref="loginForm"
      v-model="valid"
      @submit="onSubmit"
    )
      v-text-field(
        v-model="form.username"
        :rules="usernameRules"
        label="Username"
        required
      )
      v-text-field(
        type="password"
        v-model="form.password"
        :rules="passwordRules"
        label="Password"
        required
      )
      v-btn(type="submit" outline color="primary") Login
</template>

<script>
import {
  FlashedMessages
} from '@/components/'

import { MessageBus } from '@/store/messages'

export default {
  name: 'login',
  components: {
    FlashedMessages
  },
  data () {
    // {% import "bootstrap/utils.html" as utils %}
    // {% import "bootstrap/wtf.html" as wtf %}
    return {
      valid: true,
      msg: 'Login to your account',
      form: {
        username: '',
        password: ''
      },
      usernameRules: [
        v => !!v || 'Username is required'
      ],
      passwordRules: [
        v => !!v || 'Password is required'
      ]
    }
  },
  methods: {
    onSubmit () {
      if (!this.$refs.loginForm.validate()) { return }
      this.$store.dispatch('user/login', this.form).then(response => {
        this.form.password = ''
      })
    }
  },
  mounted () {
    // this.$store.dispatch('flash/load')
    MessageBus.$on('authenticated', isAuthenticated => {
      if (isAuthenticated) {
        console.log('authenticated')
        this.$router.push('/')
      }
    })
  },
  beforeDestroy () {
    MessageBus.$off('authenticated')
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
