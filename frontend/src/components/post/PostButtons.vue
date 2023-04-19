<template>
    <div class="row m-2 post-buttons">
        <!-- {% if post.likes | length > 0 %} -->
        <a
            v-if="likes.length > 0"
            data-bs-toggle="modal"
            data-bs-target="#post-likes"
            class="col"
        >
            <div v-if="likes.length == 1" class="col">
                Liked by {{ likes[0].author.username }}
            </div>
            <div v-else-if="likes.length == 2" class="col">
                Liked by {{ likes[0].author.username }} and
                {{ likes[1].author.username }}
            </div>
            <div v-else class="col">
                Liked by {{ likes[0].author.username }},
                {{ likes[1].author.username }} and others
            </div>
        </a>

        <div class="col d-flex flex-row-reverse">
            <!-- {% if current_user.id == post.author_id %} -->

            <div v-if="this.$store.getters.isAuthenticated">
                <button
                    class="btn btn-outline-danger"
                    data-bs-toggle="modal"
                    data-bs-target="#del-post1"
                >
                    <span
                        class="fa fa-solid fa-trash"
                        aria-hidden="true"
                    ></span>
                </button>
                <button
                    class="btn btn-outline-dark"
                    data-bs-toggle="modal"
                    data-bs-target="#edit-post1"
                >
                    <i class="fa fa-solid fa-pen-to-square"></i>
                </button>
            </div>
            <!-- {% endif %} -->

            <button v-if="userLikedPost" @click="likePost" class="btn btn-outline-danger">
                {{ likes.length }} <i class="fa-solid fa-heart"></i>
            </button>
            <button v-else @click="likePost" class="btn btn-outline-danger">
                {{ likes.length }} <i class="fa-regular fa-heart"></i>
            </button>

        </div>
    </div>
</template>

<script>
    import { getLikedUsers, likePost } from '@/api';
    export default {
        name: "PostButtons",
        props: {
            post: Object
        },
        data() {
            return {
                likes: []
            }
        },
        computed: {
            userLikedPost() {
                return this.likes.some(like => like.author.username == this.$store.state.userData.username)
            }
        },
        methods: {
            likePost() {
                likePost(this.$store.state.token, this.post.id)
                .then((data) => {
                    if(data.liked)
                        this.likes.push(data)    
                    else {
                        this.likes = this.likes.filter(like => like.author.username != this.$store.state.userData.username)
                        console.log(this.likes.length)
                    }
                })
            }
        },
        mounted() {
           getLikedUsers(this.post.id)
           .then((data) => {
                this.likes = data
           }) 
        },
        componenets: {
            post: Object
        }

    };
</script>

<style scoped></style>
