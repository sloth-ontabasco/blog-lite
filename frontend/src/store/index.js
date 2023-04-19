import Vuex from "vuex";

import { getImageURL, authenticate } from "@/api";
import { isValidJwt, emitter } from "@/utils/index.js";

const store = new Vuex.Store({
    state: {
        userData: null,
        token: "",
        ref_token: "",
        defaultPfpURL: null,
    },
    getters: {
        isAuthenticated(state) {
            return isValidJwt(state.token);
        },
        userID(state) {
            return state.userData ? state.userData.id : null
        }
    },
    mutations: {
        setUserData(state, payload) {
            console.log(payload)
            state.userData = Object.assign({},payload);
            if (payload.userData)
                localStorage.setItem(
                    "userData",
                    JSON.stringify(payload.userData)
                );
            else localStorage.setItem("userData", JSON.stringify(payload));
            console.log("userData state = ",state.userData)
        },
        removeUserData(state) {
            console.log("inside remove user data mutation ");
            state.userData = {};
            localStorage.removeItem("userData");
        },
        setDefaultPfpURL(state, payload) {
            state.defaultPfpURL = payload;
            localStorage.setItem("defaultPfp", payload);
            console.log("setDefaultPfpURL mutation")
            console.log(state.defaultPfpURL)
        },
        setJwtToken(state, payload) {
            console.log("setJwtToken payload = ", payload);
            localStorage.setItem("token", payload.token);
            state.token = payload.token;
            console.log(state.token);
        },
        removeJwtToken(state) {
            localStorage.removeItem("token");
            state.token = "";
        },
        setRefToken(state, payload) {
            console.log("setRefToken payload = ", payload);
            localStorage.setItem("ref_token", payload.ref_token);
            state.ref_token = payload.ref_token;
        },
    },
    actions: {
        async login(context, userData) {
            console.log("inside login action")
            const data = await authenticate(userData);
            console.log("called authenticate api call", data)
            context.commit("setJwtToken", { token: data.token });
            context.commit("setRefToken", { ref_token: data.ref_token });
            context.commit(
                "setUserData",
                Object.assign(userData, { id: data.id })
            );
            context.dispatch("getDefaultPfpURL");
        },
        getDefaultPfpURL(context) {
            console.log("Inside default pfp action");
            getImageURL("profile_pictures/default.png").then((url) =>
                context.commit("setDefaultPfpURL", url)
            );
        },
    },
    modules: {},
});

export default store;