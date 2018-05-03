var merge = require('webpack-merge')
var prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',

  // API_BASE_URL: "'http://localhost:3001/'",
  API_BASE_URL: JSON.stringify(process.env.API_BASE_URL)
  // API_BASE_URL: process.env.API_BASE_URL
})
