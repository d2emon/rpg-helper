import axios from 'axios'
import { MessageBus } from '../messages'

const api = process.env.API_BASE_URL

const state = {
  user: null,
  token: null
}

const getters = {
  isAuthenticated: state => {
    console.log('Authenticated ', state.token)
    if (!state.token || state.token.split('.').length < 3) {
      return false
    }
    const data = JSON.parse(atob(state.token.split('.')[1]))
    const exp = new Date(data.exp * 1000)
    const now = new Date()
    console.log(data)
    console.log(exp)
    console.log(now)
    return now < exp
  }
}

const mutations = {
  setUser: (state, user) => {
    state.user = user
  },
  setToken (state, token) {
    // localStorage.token = token
    state.token = token
  }
}

const actions = {
  register: (context, user) => {
    // context.commit('setUserData', { userData })
    console.log(user)
    return axios.post(api + '/register', user).then(response => {
      console.log(response.data)
      context.commit('setUser', response.data.user)
      MessageBus.$emit('newMessage', response.data.message)
      context.dispatch('login', user)
    }).catch(e => {
      console.error('Error Registering: ', e)
      MessageBus.$emit('newError', e)
    })
  },
  login: (context, user) => {
    // context.commit('setUserData', { userData })
    console.log(user)
    return axios.post(api + '/login', user).then(response => {
      console.log(response.data)
      context.dispatch('flash/load', null, { root: true })
      context.commit('setUser', user)
      context.commit('setToken', response.data.token)
      MessageBus.$emit('newMessage', response.data.token)
      MessageBus.$emit('authenticated', context.getters.isAuthenticated)
    }).catch(e => {
      console.error('Error Authenticating: ', e)
      MessageBus.$emit('newError', e.response.data.message)
    })
  },
  logout: (context) => {
    context.commit('setToken', null)
    context.commit('setUser', null)
    MessageBus.$emit('newMessage', 'You have successfully been logged out.')
  }
  // submitNewSurvey (context, survey) {
  //   let jwt = context.state.jwt.token
  //   return axios.post(`${API_URL}/surveys/`, survey, { headers: { Authorization: `Bearer: ${jwt}` } })
  // }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
