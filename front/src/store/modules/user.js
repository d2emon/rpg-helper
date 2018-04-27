import axios from 'axios'

const api = 'http://127.0.0.1:5000/api'

const state = {
  user: null
}

const getters = {}

const mutations = {
  setUser: (state, user) => {
    state.user = user
  }
}

const actions = {
  register: (context, user) => {
    console.log(user)
    axios.post(api + '/register', user).then(response => {
      console.log(response.data)
      context.commit('setUser', response.data.user)
      context.dispatch('flash/load', null, { root: true })
      context.commit('flash/addMessage', {
        message: response.data.message
      }, { root: true })
    }).catch(e => {
      console.error(e)
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
