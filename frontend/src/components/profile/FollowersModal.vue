<template>
    <div class="modal fade" id="show-followers" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{ user.username }}'s followers</h5>
                </div>
                <div class="modal-body">
                    <ul class="list-group">
                        <li
                            v-for="follower in followers"
                            class="list-group-item"
                        >
                            <img class="pfp" :src="resolvePfp(follower.id)" />
                            <router-link
                                :to="{
                                    name: 'user',
                                    params: { id: follower.id },
                                }"
                            >
                                {{ follower.username }}
                            </router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import { getUser } from '@/api';
    export default {
        name: "FollowersModal",
        props: ["user"],
        data() {
            return {
                followers: [],
                followed: [],
            }
        },
        // computed: {
        //     async followers() {
        //         console.log("computing followers");
        //         let res = [];
        //         for (const id of this.user.followers) {
        //             try {
        //                 const data = await getUser(id);
        //                 console.log(data);
        //                 res.push(data);
        //             } catch (e) {
        //                 console.log(e);
        //             }
        //         }
        //         console.log("computed followers", res);
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
            for(const id of this.user.followers) {
                try {
                    const data = await getUser(id)
                    res.push(data)
                } catch (e) {
                    console.log(e)
                }
            }
            console.log(res)
            this.followers = res;
        }
    };
</script>
