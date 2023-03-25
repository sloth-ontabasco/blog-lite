<template>
  <div class="comment-section container mt-4">
    <h3 class="h-4">Comments</h3>
    {% if post.comments | length == 0%}
    <p>This post has no comments, be the first one to post one</p>
    {% else %} {% for comment in post.comments %}
    <div class="row d-flex align-items-center mt-1">
      <figure>
        <blockquote class="blockquote">
          <p>{{ comment.content }}</p>
        </blockquote>
        <figcaption class="blockquote-footer">
          <img
            class="comment-pfp m-1"
            src="/static/profile_pictures/{{comment.user.id}}.png"
            onerror="this.onerror=null; this.src='/static/profile_pictures/default.png'"
          />
          <a href="/user/{{comment.user.id}}">{{ comment.user.username }}</a>
          commented at
          <cite>{{ comment.created_on }}</cite>
        </figcaption>
      </figure>
    </div>
    {% endfor %} {% endif %}
  </div>
</template>

<script>
    export default {
        
    }
</script>

<style  scoped>

</style>