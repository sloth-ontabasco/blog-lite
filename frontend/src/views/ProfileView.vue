<template>
    <Profile v-if="user != null" :user="user"/>
    <FollowersModal v-if="user != null" :user="user"></FollowersModal>
    <FollowedModal v-if="user != null" :user="user"></FollowedModal>
</template>


<script>
    import { getUser } from "@/api";
    import FollowedModal from "@/components/profile/FollowedModal.vue";
    import FollowersModal from "@/components/profile/FollowersModal.vue";
    import Profile from "@/components/Profile.vue";
    export default {
        name: "ProfileView",
        data() {
            return {
                user: null
            }
        },
        async mounted() {
            console.log("mounted prpofile view",this.$route.params)
            const data = await getUser(this.$route.params.id)
            this.user = data;
            console.log("got user",this.user)
        },
        methods: {
            async resolvePfp(id) {
                let pfp = null;
                try {
                    pfp = await getImageURL("profile_pictures/" + id + ".png");
                } catch (e) {
                    pfp = this.$store.state.defaultPfpURL;
                }
                return pfp;
            },
        },
        components: {
            FollowedModal,
            FollowersModal,
            Profile
        }
    };
</script>
