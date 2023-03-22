<template>
  <div class="container">
    <div
      v-if="!userHasPosts"
      class="user-noposts-alert alert alert-info alert-dismissible fade show"
      role="alert"
    >
      <strong>Your feed is empty! </strong>Follow someone or
      <a data-bs-toggle="modal" data-bs-target="#make-post">make a post</a>
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
        <PostCard v-for="post in this.posts" post="post" />
      </div>
    </div>
  </div>
  <AddPostModal />

  <div
    v-if="postSuccess"
    class="user-success-alert alert alert-success alert-dismissible fade show"
    role="alert"
  >
    <strong>Post Success</strong> View it <a href="/posts/{{post_id}}">here</a>
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
    <strong>Uh oh, Something went wrong.</strong> Please try again
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
    ></button>
  </div>
</template>

<script>
// @ is an alias to /src
import AddPostModal from '@/components/AddPostModal.vue'
import PostCard from '@/components/PostCard.vue'
import { getHomePage } from '@/api/index.js'
export default {
  name: 'HomeView',
  data() {
    return {
      posts: null,
      postSuccess: null
    }
  },
  computed: {
    userHasPosts () {
      return this.posts != null;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated
    }
  },
  async mounted() {
    if(!this.isAuthenticated) {
      if(!localStorage.token){
        this.$store.commit('removeJwtToken');
        return this.$router.push("/login")
      }
      else
        this.$store.commit("setJwtToken", { jwt: localStorage.token })
    }
    const token = this.$store.state.jwt
    console.log("token@@" + token)
    const data = await getHomePage(token)
    this.posts = data.posts;
  },
  components: {
    AddPostModal,
    PostCard
  }
}
</script>
