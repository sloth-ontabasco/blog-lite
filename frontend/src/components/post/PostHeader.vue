<template>
    <div class="post-header row align-items-center mb-2">
        <div class="col col-1 d-flex flex-row">
            <img class="pfp" :src="pfpURL" />
        </div>
        <div class="col col-1 align-self-center text-left">
            <p class="h5">
                <router-link
                    :to="{ name: 'user', params: { id: post.author.id } }"
                    >{{ post.author.username }}</router-link
                >
            </p>
        </div>
        <div class="col col-7 text-center">
            <p class="h3">{{ post.title }}</p>
        </div>
    </div>
</template>

<script>
    import { getImageURL } from '@/api';
    export default {
        name: "PostHeader",
        props: {
            post: Object,
        },
        data() {
            return {
                pfpURL: null,
            };
        },
        mounted() {
            getImageURL("profile_pictures/" + this.post.author.id + ".png")
                .then((url) => (this.pfpURL = url))
                .catch((e) => {this.pfpURL = this.$store.state.defaultPfpURL; console.log(this.$store.state.defaultPfpURL) });
        },
    };
</script>

<style scoped></style>
