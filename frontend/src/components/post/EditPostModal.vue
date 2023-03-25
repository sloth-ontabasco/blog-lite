<template>
<!--Modal for edit-->
  <div class="modal fade" tabindex="-1" role="dialog" id="edit-post1">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Edit Post</h5>
          <button
            type="button"
            class="close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form
            action="/edit"
            method="post"
            enctype="multipart/form-data"
            id="edit-post-form"
          >
            <div class="form-group">
              <label for="title">Title</label>
              <input
                type="text"
                class="form-control"
                name="title"
                id="title"
                value="{{post.title}}"
                required
              />
            </div>
            <input
              type="hidden"
              class="form-control"
              name="post-id"
              id="post-id"
              value="{{post.id}}"
            />
            <div class="form-group">
              <label for="content">Content</label>
              <textarea
                class="form-control"
                rows="5"
                name="content"
                id="content"
                >{{ post.description }}</textarea
              >
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="submit" form="edit-post-form" class="btn btn-primary">
            Edit Post
          </button>
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
  <!--Modal for edit-->
</template>

<script>
    export default {
        
    }
</script>

<style scoped>

</style>