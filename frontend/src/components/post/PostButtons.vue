<template>
    <div class="row m-2 post-buttons">
        <!-- {% if post.likes | length > 0 %} -->
        <a
            v-if="post.likes > 0"
            data-bs-toggle="modal"
            data-bs-target="#post-likes"
            class="col"
        >
            <!-- {% if post.likes | length == 1 %} -->
            <div v-if="post.likes.length == 1" class="col">
                Liked by {{ liked_users[0].username }}
            </div>
            <!-- {% elif post.likes | length == 2 %} -->
            <div v-else-if="post.likes.length == 2" class="col">
                Liked by {{ liked_users[0].username }} and
                {{ liked_users[1].username }}
            </div>
            <!-- {% else %} -->
            <div v-else class="col">
                Liked by {{ liked_users[0].username }},
                {{ liked_users[1].username }} and others
            </div>
            <!-- {% endif %} -->
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

            <form
                target="dummyframe"
                :action="'/api/post/' + post.id + '/like'"
                method="post"
                onsubmit="location.reload();"
            >
                <input
                    type="hidden"
                    class="form-control"
                    name="author_id"
                    :value="this.$store.state.userData.id"
                    style="display: none"
                />
                <!-- {% if liked == True %} -->
                <button v-if="userLikedPost" type="submit" class="btn btn-outline-danger">
                    {{ liked_users.length }} <i class="fa-solid fa-heart"></i>
                </button>
                <!-- {% else %} -->
                <button v-else type="submit" class="btn btn-outline-danger">
                    {{ liked_users.length }} <i class="fa-regular fa-heart"></i>
                </button>
                <!-- {% endif %} -->
            </form>
        </div>
    </div>
</template>

<script>
    import { getLikedUsers } from '@/api';
    export default {
        name: "PostButtons",
        props: {
            post: Object
        },
        data() {
            return {
                liked_users: []
            }
        },
        computed: {
            formActionLikeURL() {
                return '/api/post/' + this.post.id + '/like'
            },
            userLikedPost() {
                return this.liked_users.some(user => user.id == this.$store.state.userData.id)
            }
        },
        mounted() {
           getLikedUsers(this.post.id)
           .then((data) => {
                this.liked_users = data
           }) 
        },
        componenets: {
            post: Object
        }

    };
</script>

<style scoped></style>
