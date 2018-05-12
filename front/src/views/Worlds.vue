<template lang="pug">
v-container(fluid)
  v-layout(column)
    v-flex(sm10)
      v-toolbar(color="primary" dark)
        v-toolbar-side-icon
        v-toolbar-title Миры
        v-spacer
        v-btn(icon)
          v-icon search
        v-btn(icon href="/world/list")
          v-icon list
        v-btn(icon href="/world/add")
          v-icon add
        v-btn(icon @click="loadWorlds(true)")
          v-icon casino
      v-container(fluid grid-list-md class="grey lighten-4")
        v-layout(row wrap v-if="worlds.length")
          v-flex(
            v-for="world in worlds"
            v-bind="{ [`xs${world.flex}`]: true }"
            :key="world.id"
          )
            v-card(
              class="world-card"
            )
              v-card-media(
                :src="world.img"
                height="200px"
              )
              v-card-title(primary-title)
                div
                  .headline {{ world.title }}
                  span(class="grey--text") {{ world.subtitle }}
              v-card-actions(class="white")
                v-btn(flat small :href="'/world/' + world.id")
                  v-icon search
                  | Explore
                v-spacer
                v-btn(icon :href="'/world/' + world.id")
                  v-icon search
                v-btn(icon :href="'/world/' + world.id + '/edit'")
                  v-icon edit
                v-btn(icon)
                  v-icon delete
                v-btn(icon @click.native="switchFull(world.id)")
                  v-icon {{ (selectedId !== world.id) ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}
              v-slide-y-transition
                v-card-text(v-show="selectedId === world.id")
                  div {{ world }}
  v-layout(row)
    v-flex(sm6)
      | {{ worlds }}
    v-flex(sm6)
      v-container(fluid grid-list-md class="grey lighten-4")
        v-layout(row wrap)
          v-flex(
            v-for="world in worlds"
            v-bind="{ [`xs${world.flex}`]: true }"
            :key="world.id"
          )
            v-card
              v-card-media(
                :src="world.img"
                height="200px"
              )
                v-container(fill-height fluid)
                  v-layout(fill-height)
                    v-flex(xs12 align-end flexbox)
                      span(class="headline white--text" v-text="world.title")
</template>

<script>
export default {
  name: 'worlds',
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

// <!-- Add "scoped" attribute to limit CSS to this component only -->
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
