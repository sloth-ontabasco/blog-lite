<template>
    <div class="container mt-3">
        <PostHeader :post="post"></PostHeader>
        <div class="post-info-row row text-center h-25">
            <img class="col" :src="imgURL" />
        </div>
        <PostButtons :post="post"></PostButtons>
        <div class="row mt-4">
            <p class="h6">Created on {{ post.created_on }}</p>
        </div>
        <div class="row mt-3 mb-4">
            <div class="col">
                <p class="h5">{{ post.description }}</p>
            </div>
        </div>
        <AddComment :post="post"></AddComment>
    </div>
</template>

<script>
    import PostHeader from '@/components/post/PostHeader.vue'      
    import AddComment from '@/components/post/AddComment.vue'      
    import PostButtons from '@/components/post/PostButtons.vue'      
    import { getImageURL } from '@/api'; 
    export default {
        name: "Post",
        props: {
            post: Object
        },
        data() {
            return {
                imgURL: null
            }
        },
        mounted() {
            getImageURL("blog_pictures/" + this.post.id + ".png")
            .then(url => this.imgURL = url)
        },  
        components: {
            PostButtons,
            AddComment,
            PostHeader
        }
    };
</script>

<style scoped></style>
