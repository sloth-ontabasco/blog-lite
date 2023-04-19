import store from "@/store";
export function isValidJwt(jwt) {
    console.log(jwt);
    if (!jwt || jwt.split(".").length < 3) {
        return false;
    }
    const data = JSON.parse(atob(jwt.split(".")[1]));
    const exp = new Date(data.exp * 1000); // JS deals with dates in milliseconds since epoch
    const now = new Date();
    return now < exp;
}

export async function updateStore() {
    const token = localStorage.getItem("token")
    console.log("token = ", token)
    if (token) {
      console.log("founlocalstorage token")
      store.commit("setJwtToken",token)
      store.commit("setRefToken",localStorage.getItem("ref_token"))
    }
    if (window.localStorage.defaultPfp)
        await store.dispatch("getDefaultPfpURL", window.localStorage.defaultPfp);
    if (window.localStorage.userData) {
        store.commit(
            "setUserData",
            JSON.parse(window.localStorage.getItem("userData"))
        );
    }
}
