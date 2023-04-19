<template>
    <form class="d-flex" role="search">
        <input
            id="user-search"
            class="form-control mr-sm-2"
            type="search"
            placeholder="Search for users"
            aria-label="Search"
            data-bs-toggle="modal"
            data-bs-target="#make-search"
        />
    </form>
    <router-link to="logout">Logout</router-link>

    <router-link ref='profileLink' :to="{name: 'user',params: {id: userID}}">Profile</router-link> 
    <img v-if="pfpURL != null" :src="pfpURL" height="50" width="50" style="border-radius: 50%" />
    <UserSearchModal></UserSearchModal>
</template>

<script>
    import { getImageURL } from "@/api";
    import UserSearchModal from "@/components/UserSearchModal.vue";
    export default {
        name: "UserSearchNav",
        data() {
            return {
                pfpURL: null,
            };
        },
        computed: {
            userID() {
                return this.$store.getters.userID
            }
        },
        methods: {
            resolvePfp(id) {
                const pfp = {url:null};
                getImageURL("profile_picutes/" + id + ".png")
                .then(data => {pfp.url = data})
                .catch(e => {
                    pfp.url = this.$store.state.defaultPfpURL
                })
                return pfp.url;
            }
        },
        mounted() {
            console.log("In UserSearchNav moutned");
            getImageURL(
                "profile_pictures/" + this.userID + ".png"
            )
                .then((data) => {this.pfpURL = data; console.log("changing pfpURL in search nav",this.pfpURL)})
                .catch((e) => (this.pfpURL = this.$store.state.defaultPfpURL));
        },
        components: {
            UserSearchModal,
        },
    };
</script>
