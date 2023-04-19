<template>
        <div class="row d-flex justify-content-center">
            <div class="col">
                <h2>Posts from user</h2>
            </div>
        </div>
        <div class="row">
            <div v-if="posts == []" class="col">This user has no posts</div>
            <PostCard
                v-if="posts != []"
                v-for="(post, key) in this.posts"
                :key="key"
                :post="post"
            />
        </div>
</template>
<script>
import { getPost } from '@/api'
import PostCard from '../PostCard.vue'
export default {
    name: 'ProfilePosts',
    props: ['user'],
    data() {
        return {
            posts: []
        }
    },
    mounted() {
        for(const id of this.user.posts) {
            getPost(this.$store.state.token,id).then(data=>{
                this.posts.push(data)
            })
        }
    },
    components: {
        PostCard
    }
}
</script>