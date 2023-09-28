import '../assets/style.css'
import '@mdi/font/css/materialdesignicons.css'
import axiosPlugin from './axios'

import 'notyf/notyf.min.css'

export function registerPlugins (app) {
  app.use(axiosPlugin)
}