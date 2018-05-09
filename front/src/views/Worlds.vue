<template lang="pug">
// .container(class="content-section")
b-container
  b-row
    b-col
      flashed-messages
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
            div(v-for="world, id in worlds" :class="'col-sm-' + world.flex" :key="world.id")
              b-card(
                class="world-card"
              )
                div(slot="header")
                  h6 {{ world.title }}
                b-card(
                  overlay
                  :img-src="world.img"
                  :img-alt="world.title"
                )
                div(class="card-text" v-show="selectedId === id")
                  p {{ world }}
                div(slot="footer")
                  b-button(icon '@click'="switchFull(id)")
                    i(:class="'fa ' + (selectedId === id ? 'fa-angle-up' : 'fa-angle-down')")
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
      msg: 'Login to your account',
      selectedId: null
    }
  },
  methods: {
    loadWorlds (shuffle) {
      this.$store.dispatch('worlds/load', shuffle)
    },
    switchFull (id) {
      if (this.selectedId === id) {
        this.selectedId = null
      } else {
        this.selectedId = id
      }
    }
  },
  mounted () {
    this.$store.dispatch('worlds/load', false)
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

.world-card {
  margin-bottom: 10px;
}
</style>
