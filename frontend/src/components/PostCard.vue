<template>
        <div class="card mt-4 w-50">
            <img src="/static/blog_pictures/{{ post['id'] }}.png" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title"> {{ post['title'] }} </h5>
                    <p class="card-text">{{ post.description | truncate(150,True,'...') }}</p>
                    <a href="/posts/{{post.id}}" class="btn btn-primary">View Post</a>
            </div>
            <div class="card-footer">
                <div class="card-author-info d-flex align-items-center">
                    <img class="comment-pfp m-1" src="/static/profile_pictures/{{post.user.id}}.png"
                        onerror="this.onerror=null; this.src='/static/profile_pictures/default.png'" />
                    <p>&nbsp; &nbsp;<a href="/users/{{post.user.id}}">{{post.user.username}}</a> posted at {{post.created_on}}</p>
                </div>
                <div class="card-post-info">
                    <i class="fa-regular fa-heart"></i>  {{post.likes | length}}   
                    <i class="fa-regular fa-comment"></i> {{ post.comments | length }}
                </div>
            </div>
        </div>
</template>
<script>
export default  {
    name: "PostCard",
    props: ['post']
}
</script>
<style></style>