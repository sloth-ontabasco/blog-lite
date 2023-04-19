<template>
    <div
        v-if="editSuccess == true"
        class="user-success-alert alert alert-success alert-dismissible fade show"
        role="alert"
    >
        <strong>Post edited successfully</strong>

        <button
            type="button"
            class="btn-close"
            data-bs-dismiss="alert"
            aria-label="Close"
            @click="editSuccess=null"
        ></button>
    </div>

    <div
        v-if="editSuccess == false"
        class="user-success-alert alert alert-danger alert-dismissible fade show"
        role="alert"
    >
        <strong>Could not edit post:</strong>
        {{ errorMsg }}
        <button
            type="button"
            class="btn-close"
            data-bs-dismiss="alert"
            aria-label="close"
            @click="editSuccess=null"
        ></button>
    </div>

    <Post v-cloak :post="post"></Post>
    <CommentSection :post="post"></CommentSection>
    <EditPostModal @editPostCalled="handleEditPost" :post="post"></EditPostModal>
    <DeletePostModal :post="post"></DeletePostModal>
    <AllLikesModal :post="post"></AllLikesModal>
</template>

<script>
    import CommentSection from "@/components/post/CommentSection.vue";
    import EditPostModal from "@/components/post/modals/EditPostModal.vue";
    import DeletePostModal from "@/components/post/modals/DeletePostModal.vue";
    import AllLikesModal from "@/components/post/modals/AllLikesModal.vue";
    import Post from "@/components/Post.vue";
    import { getPost } from "@/api/index.js";
    export default {
        name: "PostView",
        data() {
            return {
                post: {},
                editSuccess: null,
                errorMsg: null
            };
        },
        methods: {
            handleEditPost(payload) {
                this.editSuccess=payload.success;
                if(!payload.success) {
                    this.errorMsg = payload.msg;
                } else {
                    this.post.title = payload.data.title;
                    this.post.description = payload.data.description
                }
            }
        },
        async beforeMount() {
            console.log("In post page");
            if (!localStorage.token) {
                console.log("cant find token in localstorage");
                this.$store.commit("removeJwtToken");
                return this.$router.push("/login");
            }

            getPost(this.$store.state.token, this.$route.params.id)
                .then((data) => {
                    this.post = data;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        components: {
            Post,
            CommentSection,
            AllLikesModal,
            DeletePostModal,
            EditPostModal,
        },
    };
</script>

<style scoped></style>
