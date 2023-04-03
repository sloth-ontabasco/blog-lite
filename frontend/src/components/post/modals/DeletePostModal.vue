<template>
    <!--Delete confirmation modal-->
    <div class="modal fade" role="dialog" id="del-post1">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Are you sure?</h5>
                </div>
                <div class="modal-body">
                    <p class="p-5">This action cannot be undone</p>
                    <form
                        action="/delete"
                        method="post"
                        enctype="multipart/form-data"
                        id="del-post-form"
                    >
                        <input
                            type="hidden"
                            class="form-control"
                            name="post-id"
                            id="post-id"
                            :value="post.id"
                        />
                    </form>
                </div>
                <div class="modal-footer">
                    <button
                        type="submit"
                        form="del-post-form"
                        class="btn btn-danger"
                    >
                        Delete
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
    <!--Delete confimation modal-->
</template>

<script>
    export default {
        name: "DeletePostModal",
        props: {
            post: Object
        }
    };
</script>

<style lang="scss" scoped></style>
