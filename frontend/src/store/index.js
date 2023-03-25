import { createStore } from "vuex";

import { addPost, authenticate } from "@/api";
import { isValidJwt, emitter} from "@/utils/index.js";

export default createStore({
  state: {
    userData: {},
    token: "",
    ref_token: ""
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
      localStorage.setItem("token",  payload.token)
      state.token = payload.token;
      console.log(state.token)
    },
    removeJwtToken(state) {
      localStorage.removeItem('token');
      state.token = "";
    },
    setRefToken(state, payload) {
      console.log("setRefToken payload = ", payload)
      localStorage.setItem("ref_token",  payload.ref_token)
      state.ref_token = payload.ref_token
    }
  },
  actions: {
    login(context, userData) {
      context.commit("setUserData", { userData });
      return authenticate(userData)
        .then((data) => {
          context.commit("setJwtToken", { token: data.token })
          context.commit("setRefToken", { ref_token: data.ref_token })
        })
    },
  },
  modules: {},
});

