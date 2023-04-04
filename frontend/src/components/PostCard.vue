<template>
        <div class="card mt-4 w-50">
            <img :src="imgURL" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title"> {{post.title}} </h5>
                    <p class="card-text">{{post.description.slice(0,50)}}</p>
                    <router-link :to="'/posts/' + post.id" class="btn btn-primary">View Post</router-link>
            </div>
            <div class="card-footer">
                <div class="card-author-info d-flex align-items-center">
                    <img class="comment-pfp m-1" :src="pfpURL"/>
                    <p>&nbsp; &nbsp;<router-link :to="'/users/' + post.author.id">{{post.author.username}}</router-link> posted at {{post.created_on}}</p>

                </div>
                <div class="card-post-info">
                    <i class="fa-regular fa-heart"></i>  {{post.likes}}   
                    <i class="fa-regular fa-comment"></i> {{post.comments}}
                </div>
            </div>
        </div>
</template>
<script>
import { getImageURL } from '@/api';
export default  {
    name: "PostCard",
    props: {
        post: Object
    },
    data () {
        return {
            imgURL: null,
            pfpURL: null
        }
    },
    mounted() {
        getImageURL("blog_pictures/" + this.post.id + ".png") 
        .then(url => this.imgURL = url)

        getImageURL("profile_pictures/" + this.post.author.id + ".png") 
        .then(url => this.imgURL = url)
        .catch(e => this.pfpURL = this.$store.state.defaultPfpURL)
    }
}
</script>
<style></style>