import { createStore } from "vuex";

import { addPost, authenticate } from "@/api";
import { isValidJwt, emitter} from "@/utils/index.js";

export default createStore({
  state: {
    userData: {},
    jwt: "",
  },
  getters: {
    isAuthenticated(state) {
      return isValidJwt(state.jwt);
    },
  },
  mutations: {
    setUserData(state, payload) {
      console.log("setUserData payload = ", payload);
      state.userData = payload.userData;
    },

    setJwtToken(state, payload) {
      console.log("setJwtToken payload = ", payload);
      localStorage.token = payload.jwt;
      state.jwt = payload.jwt;
    },
    removeJwtToken(state) {
      localStorage.removeItem('token');
      state.jwt = "";
    }
  },
  actions: {
    login(context, userData) {
      context.commit("setUserData", { userData });
      return authenticate(userData)
        .then((data) => {
          context.commit("setJwtToken", { jwt: data.token })
        })
    },
  },
  modules: {},
});

