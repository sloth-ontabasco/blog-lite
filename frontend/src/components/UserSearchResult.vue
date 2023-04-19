<template>
    <div id="user-display" class="container container-fluid">
        <div class="col col-3">
            <img class="pfp" :src="pfpURL" />
        </div>
        <div class="col col-6">
            <router-link :to="{ name: 'user', params: { id: user.id },replace:true }">
                <input
                    class="form-control text-center"
                    name="username"
                    type="text"
                    :value="user.username"
                    readonly
                />
            </router-link>
        </div>
        <div class="col col-3 cll">
            <button
                @click="relateUser(user)"
                :class="btnClasses"
            >
                {{ user.is_following ? "Unfollow" : "Follow" }}
            </button>
        </div>
    </div>
</template>

<script>
    import { followUser, unfollowUser, getImageURL } from "@/api";
    export default {
        name: "UserSearchResult",
        props: ["user"],
        data() {
            return {
                pfpURL: null,
            };
        },
        computed: {
            btnClasses() {
                return {
                    "btn": true,
                    "btn-success": !this.user.is_following,
                    "btn-danger": this.user.is_following,
                };
            },
        },
        methods: {
            relateUser(userObj) {
                console.log(userObj)
                if (userObj.is_following) {
                    unfollowUser(this.$store.state.token, userObj.username)
                        .then((data) => {
                            this.user.is_following = !this.user.is_following;
                        })
                        .catch((e) => console.log(e));
                } else {
                    followUser(this.$store.state.token, userObj.username)
                        .then((data) => {
                            this.user.is_following = !this.user.is_following;
                        })
                        .catch((e) => console.log(e));
                }
            },
        },
        mounted() {
            getImageURL("profile_pictures/" + this.user.id + ".png")
                .then((url) => (this.pfpURL = url))
                .catch((e) => {
                    this.pfpURL = this.$store.state.defaultPfpURL;
                    console.log(this.$store.state.defaultPfpURL);
                });
        },
    };
</script>
