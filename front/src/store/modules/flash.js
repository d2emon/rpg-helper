import axios from 'axios'

const api = process.env.API_BASE_URL

const state = {
  messages: []
}

const getters = {}

const mutations = {
  setMessages: (state, messages) => {
    state.messages = messages
  },
  addMessage: (state, message) => {
    console.log(message)
    state.messages.push(message)
  }
}

const actions = {
  load: context => {
    context.commit('setMessages', [])
    axios.get(api + '/messages').then(response => {
      let messages = response.data
      messages.forEach(item => {
        context.commit('addMessage', {
          full: item,
          category: item[0],
          message: item[1]
        })
      })
    }).catch(e => {
      console.error(e)
      context.commit('addMessage', {
        category: 'error',
        message: e
      })
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
