<template>
    <div class="row">
        <form class="mt-5 col" target="dummyframe" :action="postCommentFormURL" method="post"
            onsubmit="location.reload();">
            <div class="form-floating">
                <textarea class="form-control" name="content" placeholder="Leave a comment here" id="floatingTextarea2"
                    style="height: 150px"></textarea>
                <label for="floatingTextarea2">Leave a comment</label>
            </div>
            <!-- <input type="hidden" class="form-control" name="author_id" :value="{{current_user.id}}" /> -->
            <button type="submit" class="btn btn-outline-success btn-lg mt-4">Post</button>
        </form>
    </div>
</template>

<script>
    export default {
       name: 'AddComment',
       props: {
            post: Object
       },
       computed: {
            postCommentFormURL() {
                return "/api/post/" + this.post.id + "/comment"
            }
       } 
    }
</script>

<style scoped>

</style>