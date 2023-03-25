<template>
    <div class="container mt-3">

        <div class="post-header row align-items-center mb-2">
            <div class="col col-1 d-flex flex-row">
                <img
                    class="pfp"
                    src="/static/profile_pictures/{{post.user.id}}.png"
                    onerror="this.error = null; this.src = '/static/profile_pictures/default.png'"
                />
            </div>
            <div class="col col-1 align-self-center text-left">
                <p class="h5">
                    <a href="/users/{{post.user.id}}">{{ post.user.username }}</a>
                </p>
            </div>
            <div class="col col-7 text-center">
                <p class="h3">{{ post.title }}</p>
            </div>
        </div>

        <div class="post-info-row row text-center h-25">
            <img class="col" src="/static/blog_pictures/{{post.id}}.png" />
        </div>

        <PostButtons></PostButtons>

        <div class="row mt-4">
            <p class="h6">Created on {{ post.created_on }}</p>
        </div>

        <div class="row mt-3 mb-4">
            <div class="col">
                <p class="h5">{{ post.description }}</p>
            </div>
        </div>

        <AddComment></AddComment>
    </div>

    <CommentSection></CommentSection>

    <EditPostModal></EditPostModal>

    <DeletePostModal></DeletePostModal>

  
  </template>

<script>
export default {};
</script>

<style scoped></style>
