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
                        id="edit-post-form"
                    >
                        <div class="form-group">
                            <label for="title">Title</label>
                            <input
                                type="text"
                                class="form-control"
                                name="title"
                                id="title"
                                v-model="title"
                            />
                        </div>
                        <div class="form-group">
                            <label for="content">Content</label>
                            <textarea
                                class="form-control"
                                rows="5"
                                name="content"
                                v-model="description"
                                id="content"
                            >
                            </textarea>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button
                        @click="editPost"
                        class="btn btn-primary"
                        data-bs-dismiss="modal"
                    >
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
    import { editPost } from '@/api';
    export default {
        name: "EditPostModal",
        props: {
            post: Object
        },
        data() {
            return {
                title: this.post.title,
                description: this.post.description
            }
        },
        methods: {
            editPost() {
                editPost(this.$store.state.token, this.post.id, {
                    title: this.title,
                    description: this.description
                })
                .then((data) => {
                    this.$emit("editPostCalled",{success: true, data: data})
                    // this.$router.push({name: this.$route.name, query: {editPost: "success"}})
                })
                .catch((e) => {
                    this.$emit("editPostCalled",{success: false, msg: e})
                    // this.$router.push({name: this.$route.name, query: {editPost: "failure",msg: e}})
                })
            }
        }
    };
</script>

<style scoped></style>
