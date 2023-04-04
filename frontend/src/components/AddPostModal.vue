<template>
    <!--Modal for submission-->
    <div class="modal fade" tabindex="-1" role="dialog" id="make-post1">
        <div class="modal-dialog" role="document">
            <div class="modal-content">

                <div class="modal-header">
                    <h5 class="modal-title">Create Post</h5>
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
                    <form id="make-post-form">
                        <div class="form-group">
                            <div class="preview">
                                <img id="file-ip-1-preview" />
                            </div>
                            <label for="file-upload">Upload Cover Picture</label
                            ><br />
                            <input
                                type="file"
                                id="file-upload"
                                name="file-upload"
                                accept="image/*"
                                required
                            />
                        </div>
                        <div class="form-group">
                            <label for="title">Title</label>
                            <input
                                type="text"
                                class="form-control"
                                v-model="title"
                                name="title"
                                id="title"
                                placeholder="Enter Post Title"
                                required
                            />
                        </div>

                        <div class="form-group">
                            <label for="content">Content</label>
                            <textarea
                                class="form-control"
                                rows="5"
                                v-model="description"
                                name="content"
                                id="content"
                                placeholder="Content"
                            ></textarea>
                        </div>
                    </form>
                </div>

                <div class="modal-footer">
                    <button @click="createPost" class="btn btn-primary" data-bs-dismiss="modal">Create Post</button>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <div
        class="button iconbutton"
        data-bs-toggle="modal"
        data-bs-target="#make-post1"
    >
        <i class="fa-solid fa-plus"></i>
    </div>
    <!--Modal for submission-->
</template>
<script>
    import { addPost } from "@/api/index.js";
    export default {
        name: "AddPostModal",
        data() {
            return {
                description: "",
                title: "",
                file: null,
            };
        },
        methods: {
            createPost() {
                const token = this.$store.state.token;
                let form = new FormData()
                let img = document.getElementById('file-upload')

                form.append("title",this.title)
                form.append("description",this.description)

                if(img.files[0])
                    form.append("image",img.files[0])

                addPost(token, form)
                .then((data) => {
                    this.$emit("addPostCalled",{
                        "postSuccess":true,
                        "data": data
                    })
                })
                .catch((e) => {
                    console.log(e.message)
                    this.$emit("addPostCalled",{
                        "postSuccess": false,
                        "data": e.message
                    })
                })
            },
        },
        emits: ['addPostCalled']
    };
</script>
<style scoped></style>
