<template>
<!--Modal for submission-->
<div class="modal fade" tabindex="-1" role="dialog" id="make-post1">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Create Post</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form action="/post" method="post" enctype="multipart/form-data" id="make-post-form">

                    <div class="form-group">
                        <div class="preview">
                            <img id="file-ip-1-preview">
                        </div>
                        <label for="file-upload">Upload Cover Picture</label><br>
                        <input type="file" id="file-upload" name="file-upload" accept="image/*"
                            onchange="showPreview(event);" required>
                    </div>
                    <div class="form-group">
                        <label for="title">Title</label>
                        <input type="text" class="form-control" name="title" id="title" placeholder="Enter Post Title"
                            required>
                    </div>

                    <div class="form-group">
                        <label for="content">Content</label>
                        <textarea class="form-control" rows="5" name="content" id="content"
                            placeholder="Content"></textarea>
                    </div>
                </form>
            </div>
        </div>
        <div class="modal-footer">
            <button type="submit" form="make-post-form" class="btn btn-primary">Create Post</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        </div>
    </div>
</div>
<div class="button iconbutton" data-bs-toggle="modal" data-bs-target="#make-post1">
    <i class="fa-solid fa-plus"></i>
</div>
<!--Modal for submission-->
</template>
<script>
export default {
    name: "AddPostModal"
}
</script>
<style scoped>
</style>