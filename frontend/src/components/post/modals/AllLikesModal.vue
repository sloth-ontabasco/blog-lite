<template>
    <div class="modal fade" tabindex="-1" role="dialog" id="post-likes">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">All Likes</h5>
                </div>
                <div class="modal-body">
                    <ul class="list-group">
                        <li v-for="(like,id) in likes" :key="id" class="list-group-item">
                            <img
                                class="pfp"
                                :src="pfpURL"
                            />
                            <router-link :to="{name: 'user', params: {id: like.author.id}}">{{like.author.username}}</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { getLikedUsers, getImageURL } from '@/api';
    export default {
        name: "AllLikesModal",
        props: {
            post: Object
        },
        data() {
            return {
                likes: [],
                pfpURL: null
            }
        },
        mounted() {
            getLikedUsers(this.post.id)
            .then(data => this.likes = data)

            getImageURL("profile_pictures/" + this.post.author.id + ".png")
            .then(data => this.pfpURL = data)
            .catch(e => this.pfpURL = this.$store.state.defaultPfpURL)
        }
    };
</script>

<style scoped></style>
