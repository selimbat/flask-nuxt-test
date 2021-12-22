export default {
  ssr: false,
  target: "static",

  buildModules: ["@nuxtjs/vuetify"],
  modules: ["@nuxtjs/axios"],

  axios: {
    baseURL: process.env.API_URL || "http://localhost:8000/",
    browserBaseURL: process.env.API_URL || "http://localhost:8000/",
  },
};
