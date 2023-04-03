<template>
    <div class="comment-section container mt-4">
        <h3 class="h-4">Comments</h3>
        <!-- {% if post.comments | length == 0%} -->
        <p v-if="comments.length == 0">This post has no comments, be the first to post one</p>
        <!-- {% else %} {% for comment in post.comments %} -->
        <div v-else v-for="(comment,id) in comments" :key="id" class="row d-flex align-items-center mt-1">
            <figure>
                <blockquote class="blockquote">
                    <p>{{ comment.content }}</p>
                </blockquote>
                <figcaption class="blockquote-footer">
                    <img
                        class="comment-pfp m-1"
                        :src="'/static/profile_pictures/' + comment.author.id + '.png'"
                        onerror="this.onerror=null; this.src='/static/profile_pictures/default.png'"
                    />
                    <router-link :to="{name: 'user', params: {id: comment.author.id}}">{{comment.author.username}}</router-link>
                    commented at
                    <cite>{{ comment.created_on }}</cite>
                </figcaption>
            </figure>
        </div>
        <!-- {% endfor %} {% endif %} -->
    </div>
</template>

<script>
    import { getPostComments }  from '@/api/index.js' 
    export default {
        name: "CommentSection",
        props: {
            post: Object,
        },
        data() {
            return {
                comments: [],
            };
        },
        mounted() {
            getPostComments(this.post.id)
            .then(data => this.comments = data)
        },
    };
</script>

<style scoped></style>
