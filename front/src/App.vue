<template lang="pug">
router-view
</template>

<script>
/* Import Vuetify Styles */
import 'vuetify/dist/vuetify.min.css'

export default {
  name: 'app'
}
</script>

<style lang="scss">
/* Import Font Awesome Icons Set */
/* @import '~flag-icon-css/css/flag-icon.min.css'; */
/* Import Font Awesome Icons Set */
// $fa-font-path: '~font-awesome/fonts/';
// @import '~font-awesome/css/font-awesome.min.css';
/* Import Simple Line Icons Set */
/* $simple-line-font-path: '~simple-line-icons/fonts/'; */
/* @import '~simple-line-icons/css/simple-line-icons.css'; */

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
