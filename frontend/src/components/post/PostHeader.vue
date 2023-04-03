<template>
    <div class="post-header row align-items-center mb-2">
        <div class="col col-1 d-flex flex-row">
            <img
                class="pfp"
                :src="authorPfpURL"
                @error="{this.$event = null; this.src = '/assets/profile_pictures/default.png'}"
            />
        </div>
        <div class="col col-1 align-self-center text-left">
            <p class="h5">
                <router-link :to="{name: 'user', params: {id: post.author.id}}">{{ post.author.username }}</router-link>
            </p>
        </div>
        <div class="col col-7 text-center">
            <p class="h3">{{ post.title }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "PostHeader",
        props: {
            post: Object
        },
        computed: {
            authorPfpURL() {
                console.log(this.post.id)
                return '/assets/profile_pictures/' + this.post.author.id + '.png'
            }
        }
    };
</script>

<style scoped></style>
