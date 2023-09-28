import axios from 'axios';

const axiosPlugin = {
  install(app) {
    const axiosInstance = axios.create({
      baseURL: 'http://localhost:8000/api',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    axiosInstance.interceptors.response.use(
      function(response) {
        return response
      },
      function(error) {
        return Promise.reject(error)
      }
    )

    app.provide('axios', axiosInstance);
    app.config.globalProperties.$axios = axiosInstance;
  },
};

export default axiosPlugin;