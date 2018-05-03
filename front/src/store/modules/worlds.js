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
    state.worlds = worlds
    state.worlds.forEach(item => {
      item.flex = (Math.floor(Math.random() * 3) + 1) * 3
    })
  }
}

const actions = {
  load: (context) => {
    return axios.get(api + '/world-api/list?count=100', { count: 100 }).then(response => {
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
