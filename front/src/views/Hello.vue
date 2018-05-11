<template lang="pug">
.content-section
  .intro-header
    v-container
      v-layout(row)
        v-flex(xs12)
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
  // padding-top: 50px;
  // padding-bottom: 50px;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  color: #f8f8f8;
  background: url(/static/images/intro-bg.jpg) no-repeat center center;
  background-size: cover;
  width: 1170px;
  height: 100%;
}

.intro-message {
  position: relative;
  padding-top: 20%;
  padding-bottom: 20%;
}

.intro-message > h1 {
  margin: 0;
  text-shadow: 2px 2px 3px rgba(0,0,0,0.6);
  font-size: 5em;
}

.intro-message > h3 {
    text-shadow: 2px 2px 3px rgba(0,0,0,0.6);
}

.intro-divider {
  margin-left: auto;
  margin-right: auto;
  width: 400px;
  border-top: 1px solid #f8f8f8;
  border-bottom: 1px solid rgba(0,0,0,0.2);
}
</style>
