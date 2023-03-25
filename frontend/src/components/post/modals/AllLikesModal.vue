<template>
  <div class="modal fade" tabindex="-1" role="dialog" id="post-likes">
    <div class="modal-dialog modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">All Likes</h5>
        </div>
        <div class="modal-body">
          <ul class="list-group">
            {% for like in post.likes %}
            <li class="list-group-item">
              <img
                class="pfp"
                src="/static/profile_pictures/{{like.user.id}}.png"
                onerror="this.onerror=null; this.src='/static/profile_pictures/default.png'"
              />
              <a href="/users/{{like.user.id}}">{{ like.user.username }}</a>
            </li>
            {% endfor %}
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped></style>
