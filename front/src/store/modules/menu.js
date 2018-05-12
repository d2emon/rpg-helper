const state = {
  miniVariant: false,
  clipped: true,
  fixed: false,
  navDrawer: true,
  utilityDrawer: false
}

const getters = {
}

const mutations = {
  switchMini: state => {
    state.miniVariant = !state.miniVariant
  },
  switchClipped: state => {
    state.clipped = !state.clipped
  },
  switchFixed: state => {
    state.fixed = !state.fixed
  },
  switchNavDrawer: state => {
    state.navDrawer = !state.navDrawer
  },
  setNavDrawer: (state, value) => {
    state.navDrawer = value
  },
  switchUtilityDrawer: state => {
    state.utilityDrawer = !state.utilityDrawer
  },
  setUtilityDrawer: (state, value) => {
    state.utilityDrawer = value
  }
}

const actions = {
}

export default {
  state,
  getters,
  mutations,
  actions
}
