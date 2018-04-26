<template lang="pug">
div
  | {% import "bootstrap/utils.html" as utils %}
  | {% import "bootstrap/wtf.html" as wtf %}
  .content-section
    br
    | {{ utils.flashed_messages() }}
    br
    .center
      h1 Login to your account
      br
      | {{ wtf.quick_form(form) }}
      h1 {{ appname }}
      h3 {{ msg }}

</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      appname: 'Login',
      msg: 'The best company in the world!'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

h3 {
  padding-top: 20px;
  padding-bottom: 10px;
}

.intro-header {
  width: 1170px;
}
</style>
