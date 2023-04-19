<template>
    <nav class="navbar navbar-light bg-light">
        <router-link class="navbar-brand ml-2" to="/home">
            <img src="/static/bloglite-icon.png" width="50" height="50" />
            Bloglite
        </router-link>
        <router-link v-if="authenticated" to="/home">Home</router-link>
        <router-link v-if="authenticated" to="/login">Login</router-link>
        <router-link to="/register">Register</router-link>

        <UserSearchNav v-if="authenticated"></UserSearchNav>
    </nav>
    <router-view />
</template>
<script>
    import { updateStore } from "./utils";
    import UserSearchNav from "./views/UserSearchNav.vue";
    export default {
        data() {
            return {
                pfpURL: null,
            };
        },
        computed: {
            authenticated() {
                return this.$store.getters.isAuthenticated;
            },
        },
        async mounted() {
            await updateStore()
            // console.log("In app mounted");
            // if (localStorage.token) {
            //     this.$store.state.token = localStorage.token;
            //     this.$store.state.ref_token = localStorage.ref_token;
            // }
            // if (localStorage.defaultPfp)
            //     this.$store.commit("setDefaultPfpURL", localStorage.defaultPfp);
            // if (localStorage.userData) {
            //     this.$store.commit(
            //         "setUserData",
            //         JSON.parse(localStorage.getItem("userData"))
            //     );
            //     console.log(JSON.parse(localStorage.getItem("userData")));
            // }
        },
        components: {
            UserSearchNav,
        },
    };
</script>
<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    nav {
        padding: 30px;
    }

    nav a {
        font-weight: bold;
        color: #2c3e50;
    }

    nav a.router-link-exact-active {
        color: #42b983;
    }

    .iconbutton {
        width: 60px;
        height: 60px;
        border-radius: 100%;
        background: #ff4f79;
    }

    .button {
        width: 80px;
        height: 80px;
        background: #000000;
        position: fixed;
        bottom: 60px;
        right: 60px;
    }

    .iconbutton i {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
        color: white;
    }

    .pfp {
        height: 50px;
        width: 50px;
        border-radius: 50%;
    }

    .comment-pfp {
        border-radius: 50%;
        height: 25px;
        width: 25px;
    }
</style>
