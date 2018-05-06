<template lang="pug">
// .container(class="content-section")
b-container
  b-row
    b-col
      flashed-messages
  b-row
    b-col
      h1 {{ msg }}
      b-button('@click'="loadWorlds(true)") btn
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
              i(class="fa fa-random")
        div(slot="footer") Footer Slot
        b-container
          b-row
            div(v-for="world in worlds" :class="'col-sm-' + world.flex" :key="world.id")
              b-card(class="world-card")
                b-card(
                  overlay
                  :img-src="world.src"
                  :img-alt="world.title"
                  text-variant="white"
                  :title="world.title"
                  :sub-title="world.subtitle"
                )
                b-button(icon '@click'="loadWorlds('world.show = !world.show')")
                  i(:class="'fa ' + (world.show ? 'fa-angle-down' : 'fa-angle-up')")
                p {{ world.flex }}
                p {{ world.show }}
                p(class="card-text" v-show="world.show")
                  | {{world}}
                  | I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
                div(slot="footer")
                  // b-button(icon @click.native="world.show = !world.show")
                  b-button(icon '@click'="loadWorlds('world.show = !world.show')")
                    i(:class="'fa ' + (world.show ? 'fa-angle-down' : 'fa-angle-up')")
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
      alert(load)
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

.world-card .card-body {
  height: 200px;
}

.world-card .card-img {
  // height: 200px;
}
</style>
