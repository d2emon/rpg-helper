<template lang="pug">
.container(class="content-section")
  .center
    h1.pb-3 {{ msg }}
    v-form(
      ref="regForm"
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
      v-btn(type="submit" outline color="primary") Regiister
</template>

<script>
export default {
  name: 'register',
  data () {
    // {% import "bootstrap/utils.html" as utils %}
    // {% import "bootstrap/wtf.html" as wtf %}
    return {
      valid: true,
      msg: 'Register for an account',
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
      if (!this.$refs.regForm.validate()) { return }
      this.$store.dispatch('user/register', this.form).then(response => {
        this.$store.dispatch('flash/load')
      })
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
