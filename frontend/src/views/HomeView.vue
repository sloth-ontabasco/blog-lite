<template>
    <div class="container">
        <div
            v-if="deleteSuccess"
            class="user-success-alert alert alert-success alert-dismissible fade show"
            role="alert"
        >
            <strong>Post deleted successfully</strong>

            <button
                type="button"
                class="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
            ></button>
        </div>
        <div
            v-if="postSuccess"
            class="user-success-alert alert alert-success alert-dismissible fade show"
            role="alert"
        >
            <strong>Post Success</strong> View it
            <a href="/posts/{{post_id}}">here</a>
            <button
                type="button"
                class="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
            ></button>
        </div>
        <div
            v-if="postSuccess === false"
            class="user-failure-alert alert alert-danger alert-dismissible fade show"
            role="alert"
        >
            <strong>Error: {{ error_msg }}</strong> Please try again
            <button
                type="button"
                class="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
                @click="this.error_msg=null; this.postSuccess = null;"
            ></button>
        </div>
        <div
            v-if="!userHasPosts"
            class="user-noposts-alert alert alert-info alert-dismissible fade show"
            role="alert"
        >
            <strong>Your feed is empty! </strong>Follow someone or
            <a data-bs-toggle="modal" data-bs-target="#make-post"
                >make a post</a
            >
            <button
                type="button"
                class="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
            ></button>
        </div>
        <div v-else="userHasPosts">
            <h2 class="row">Posts from your friends!</h2>
            <div class="row">
                <PostCard
                    v-for="(post, key) in this.posts"
                    :key="key"
                    :post="post"
                />
            </div>
        </div>
    </div>
    <AddPostModal @addPostCalled="handleAddPostCalled" />
</template>

<script>
    // @ is an alias to /src
    import AddPostModal from "@/components/AddPostModal.vue";
    import PostCard from "@/components/PostCard.vue";
    import { getHomePage } from "@/api/index.js";
    export default {
        name: "HomeView",
        data() {
            return {
                posts: [],
                postSuccess: null,
                error_msg: null,
                deleteSuccess: null
            };
        },
        computed: {
            userHasPosts() {
                return this.posts != null;
            },
            isAuthenticated() {
                return this.$store.getters.isAuthenticated;
            },
        },
        methods: {
            handleAddPostCalled(payload) {
                this.postSuccess = payload.postSuccess;
                if (payload.postSuccess) this.posts.push(payload.data);
                else this.error_msg = payload.data
            },
        },
        async mounted() {
            if (!localStorage.token) {
                console.log("cant find token in localstorage");
                await setTimeout(() => {},2000)
                this.$store.commit("removeJwtToken");
                return this.$router.push("/login");
            }
            const token = localStorage.getItem("token");
            const data = await getHomePage(token);
            console.log(data);
            this.posts = data;

            if(this.$route.query) {
                if(this.$route.query.deletePost)
                    this.deleteSuccess = true
            }
            console.log("Reached end of mounted")
        },
        components: {
            AddPostModal,
            PostCard,
        },
    };
</script>
