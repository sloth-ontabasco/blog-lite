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
                </div>
                <div class="modal-footer">
                    <button
                        @click="deletePost"
                        class="btn btn-danger"
                        data-bs-dismiss="modal"
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
    import { deletePost } from '@/api/index.js'
    export default {
        name: "DeletePostModal",
        props: {
            post: Object
        },
        methods: {
            async deletePost() {
                const data = await deletePost(this.$store.state.token, this.post.id)
                const navres = await this.$router.push({path: '/home', query: {deletePost: true}})
                console.log(navres)
            }
        }
    };
</script>

<style lang="scss" scoped></style>
