import axios from 'axios'

const api = 'http://127.0.0.1:5000/api'

const state = {
  flashed_messages: []
}

const getters = {}

const mutations = {
  setMessages: (state, messages) => {
    state.flashed_messages = messages
  }
}

const actions = {
  messages: context => {
    axios.get(api + '/messages').then(response => {
      /*
      let worlds = response.data.worlds
      console.debug(response.data)
      var flexes = [
        6,
        12
      ]
      this.worlds = []
      var rndFlex = 1
      for (let i = 0; i < worlds.length; i++) {
        let world = worlds[i]
        let flex = 0
        if (!rndFlex) {
          rndFlex = 1
        } else {
          rndFlex = Math.floor(Math.random() * flexes.length)
          flex = rndFlex
        }
        world.id = i
        world.flex = flexes[flex]
        this.worlds.push(world)
      }
      */
      context.commit('setMessages', response.data)
    }).catch(e => {
      console.error(e)
      context.commit('setMessages', ['ERROR'])
    })
  },
  register: (context, user) => {
    console.log(user)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
