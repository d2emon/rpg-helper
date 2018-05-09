<template lang="pug">
router-view
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="scss">
/* Import Font Awesome Icons Set */
// $fa-font-path: '~font-awesome/fonts/';
// @import '~font-awesome/css/font-awesome.min.css';

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
