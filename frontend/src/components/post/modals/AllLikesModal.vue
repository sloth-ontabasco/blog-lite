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
                                :src="'/static/profile_pictures/' + like.author.id + '.png'"
                                onerror="this.onerror=null; this.src='/static/profile_pictures/default.png'"
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
    import { getLikedUsers } from '@/api';
    export default {
        name: "AllLikesModal",
        props: {
            post: Object
        },
        data() {
            return {
                likes: []
            }
        },
        mounted() {
            getLikedUsers(this.post.id)
            .then(data => this.likes = data)
        }
    };
</script>

<style scoped></style>
