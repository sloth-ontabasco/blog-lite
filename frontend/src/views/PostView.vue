<template>
    <Post v-cloak :post="post"></Post>
    <CommentSection :post="post"></CommentSection>
    <EditPostModal :post="post"></EditPostModal>
    <DeletePostModal :post="post"></DeletePostModal>
    <AllLikesModal :post="post"></AllLikesModal>
</template>

<script>
    import CommentSection from "@/components/post/CommentSection.vue"
    import EditPostModal from "@/components/post/modals/EditPostModal.vue"
    import DeletePostModal from "@/components/post/modals/DeletePostModal.vue"
    import AllLikesModal from "@/components/post/modals/AllLikesModal.vue"
    import Post from '@/components/Post.vue'
    import { getPost } from '@/api/index.js'
    export default {
        name: "PostView",
        data() {
            return {
                post: {},
            }
        },
        async beforeMount() {
            console.log("In post page")
            if (!localStorage.token) {
                console.log("cant find token in localstorage");
                this.$store.commit("removeJwtToken");
                return this.$router.push("/login");
            }
            
            console.log(this.$route.params.id)
            getPost(this.$store.state.token, this.$route.params.id)
            .then((data) => {
                this.post = data;
            })
            .catch((e) => {
                console.log(e);
            })


        },
        components: {
            Post,
            CommentSection,
            AllLikesModal,
            DeletePostModal,
            EditPostModal
        }
    };
</script>

<style scoped></style>
