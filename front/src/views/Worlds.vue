<template lang="pug">
// .container(class="content-section")
b-container
  b-row
    b-col
      flashed-messages
  b-row
    b-col
      h1 {{ msg }}
      div(v-for="world, id in worlds" :key="id") {{ world }}
  b-row(v-if="worlds.length")
    b-col
      b-card
        b-row(slot="header")
          h6.col-sm-10 Миры
          b-col(sm="2")
            b-button(icon)
              i(class="fa fa-search")
            b-button(icon @click="loadWorlds(true)")
              i(class="fa fa-casino")
        div(slot="footer") Footer Slot
        b-container
          div(v-for="world in worlds" v-bind="{ [`xs${world.flex}`]: true }" :key="world.id")
            b-card(
              overlay
              img-src="https://lorempixel.com/900/250/sports/6/"
              img-alt="Card Image"
              text-variant="white"
              :title="world.title"
              :sub-title="world.subtitle"
              :src="world.src"
              height="200px"
            )
              div(slot="footer")
                b-button(flat) Share
                b-button(flat color="purple") Explore
                b-button(icon)
                  i(class="fa fa-favourite")
                b-button(icon)
                  i(class="fa fa-bookmark")
                b-button(icon)
                  i(class="fa fa-share")
                b-button(icon @click.native="show = !show")
                  i(:class="'fa ' + show ? 'keyboard_arrow_down' : 'keyboard_arrow_up'")
              p(class="card-text" v-show="show")
                  | I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
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
  computed: {
    worlds () { return this.$store.state.worlds.worlds }
  },
  data () {
    return {
      msg: 'Login to your account'
    }
  },
  methods: {
    loadWorlds (load) {

    }
  },
  mounted () {
    this.$store.dispatch('worlds/load')
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
