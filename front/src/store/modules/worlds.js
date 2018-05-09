import axios from 'axios'
import { MessageBus } from '../messages'

const api = process.env.API_BASE_URL

const state = {
  worlds: []
}

const getters = {
}

const mutations = {
  setWorlds: (state, worlds) => {
    var space = 12
    state.worlds = worlds
    state.worlds.forEach(item => {
      item.flex = (Math.floor(Math.random() * 3) + 1) * 3
      if (space <= item.flex) {
        item.flex = space
        space = 12
      } else {
        space -= item.flex
      }
    })
  }
}

const actions = {
  load: (context, shuffle) => {
    let count = 100
    let url = api + '/world-api/list'
    url += '?count=' + count
    if (shuffle) { url += '&random=1' }
    return axios.get(url).then(response => {
      console.log(response.data)
      context.commit('setWorlds', response.data.worlds)
    }).catch(e => {
      console.error('Error: ', e)
      MessageBus.$emit('newError', e)
      MessageBus.$emit('newError', e.response.data.message)
    })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
