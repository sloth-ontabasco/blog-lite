<template>
    <div class="modal fade" id="show-followed" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{ user.username }}'s Following</h5>
                </div>
                <div class="modal-body">
                    <ul class="list-group">
                        <li v-for="f in followed" class="list-group-item">
                            <img class="pfp" :src="resolvePfp(f.id)" />
                            <router-link
                                :to="{ name: 'user', params: { id: f.id } }"
                            >
                                {{ f.username }}
                            </router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import { getImageURL, getUser } from "@/api";

    export default {
        name: "FollowedModal",
        props: ["user"],
        data() {
            return {
                followed: []
            }
        },
        // computed: {
        //     followed() {
        //         console.log("computing followed");
        //         let res = [];
        //         for (const id of this.user.followed) {
        //                 getUser(id).then(data => {
        //                     res.push(data);
        //                 })
        //         }
        //         console.log("computed followed", Array.isArray(res), typeof(res[0]));
        //         return res;
        //     },
        // },
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
        async mounted() {
            let res = [];
            for(const id of this.user.followed) {
                try {
                    const data = await getUser(id)
                    res.push(data)
                } catch (e) {
                    console.log(e)
                }
            }
            console.log(res)
            this.followed = res;
        }
    };
</script>
