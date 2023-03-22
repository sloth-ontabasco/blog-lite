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
                <form id="make-post-form">
                    <div class="form-group">
                        <div class="preview">
                            <img id="file-ip-1-preview">
                        </div>
                        <label for="file-upload">Upload Cover Picture</label><br>
                        <input type="file" id="file-upload" name="file-upload" accept="image/*" required>
                    </div>
                    <div class="form-group">
                        <label for="title">Title</label>
                        <input type="text" class="form-control" v-model="title" name="title" id="title" placeholder="Enter Post Title"
                            required>
                    </div>

                    <div class="form-group">
                        <label for="content">Content</label>
                        <textarea class="form-control" rows="5" v-model="content" name="content" id="content"
                            placeholder="Content"></textarea>
                    </div>
                </form>
            </div>
        </div>
        <div class="modal-footer">
            <button @click="createPost" type="button" class="btn btn-primary">Create Post</button>
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
import addPost from '@/api/index.js'
export default {
    name: "AddPostModal",
    data() {
        return {
            content: "",
            title: "",
            file: null
        }
    },
    methods: {
        createPost() {
            
            console.log("createPost called")
            let form = new FormData(document.getElementById('make-post-form'))
            const postData = new URLSearchParams();
            console.log("postData: ", typeof(postData))
            for(const p of form)
                postData.append(
                    p[0], p[1]
                )
            addPost(postData)
            .then((data) => {
                console.log(data);
            })
        }
    }
}
</script>
<style scoped>
</style>