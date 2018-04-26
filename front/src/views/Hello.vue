<template lang="pug">
.intro-header
  .container
    .row
      .col-lg-12
        .intro-message
          // img(src="../assets/logo.png")
          h1 {{ appname }}
          h3 {{ msg }}
          hr.intro-divider
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      appname: 'RPG-Helper',
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
