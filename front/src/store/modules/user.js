import axios from 'axios'
import { MessageBus } from '../messages'

const api = process.env.API_BASE_URL

const state = {
  user: null,
  token: null
}

const getters = {
  userData: state => {
    // console.log('Authenticated ', state.token)
    if (!state.token || state.token.split('.').length < 3) {
      return null
    }
    return JSON.parse(atob(state.token.split('.')[1]))
  },
  isAuthenticated: (state, getters) => {
    const data = getters.userData
    if (!data) {
      return false
    }

    const exp = new Date(data.exp * 1000)
    const now = new Date()
    return now < exp
  },
  user: (state, getters) => {
    const data = getters.userData
    if (!data) {
      return null
    }

    return {
      username: data.sub,
      is_admin: true,
      after_login: '/'
    }
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
    return axios.post(api + '/register', user).then(response => {
      MessageBus.$emit('newMessage', response.data.message)
      context.dispatch('login', user)
    }).catch(e => {
      console.error('Error Registering: ', e)
      MessageBus.$emit('newError', e)
    })
  },
  login: (context, user) => {
    return axios.post(api + '/login', user).then(response => {
      context.commit('setToken', response.data.token)
      // context.commit('setUser', context.getters.user)

      // context.dispatch('flash/load', null, { root: true })
      MessageBus.$emit('authenticated', context.getters.isAuthenticated)
    }).catch(e => {
      console.error('Error Authenticating: ', e)
      MessageBus.$emit('newError', e.response.data.message)
    })
  },
  logout: (context) => {
    context.commit('setToken', null)
    context.commit('setUser', null)
    context.commit('flash/addMessage', {
      category: 'info',
      message: 'You have successfully been logged out.'
    }, {
      root: true
    })
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
