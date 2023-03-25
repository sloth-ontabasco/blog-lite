<template>
    <div class="row m-2 post-buttons">

        {% if post.likes | length > 0 %}
        <a data-bs-toggle="modal" data-bs-target="#post-likes" class="col">
            {% if post.likes | length == 1 %}
            <div class="col">Liked by {{post.likes[0].user.username}}</div>
            {% elif post.likes | length == 2 %}
            <div class="col">Liked by {{post.likes[0].user.username}} and {{post.likes[1].user.username}}</div>
            {% else %}
            <div class="col">Liked by {{post.likes[0].user.username}}, {{post.likes[1].user.username}} and others</div>
            {% endif %}
        </a>

        {% endif %}
        <div class="col d-flex flex-row-reverse">
            {% if current_user.id == post.author_id %}

            <button class="btn btn-outline-danger" data-bs-toggle="modal" data-bs-target="#del-post1"><span
                    class="fa fa-solid fa-trash" aria-hidden="true"></span></button>
            <button class="btn btn-outline-dark" data-bs-toggle="modal" data-bs-target="#edit-post1"><i
                    class="fa fa-solid fa-pen-to-square "></i>
            </button>
            {% endif %}
            

            <form target="dummyframe" action="/api/post/{{post.id}}/like" method="post" onsubmit="location.reload();">

                <input type="hidden" class="form-control" name="author_id" value="{{current_user.id}}"
                    style="display:none;" />
                {% if liked == True %}
                <button type="submit" class="btn btn-outline-danger">{{num_likes}} <i class="fa-solid fa-heart"></i></button>
                {% else %}
                <button type="submit" class="btn btn-outline-danger">{{num_likes}} <i class="fa-regular fa-heart"></i></button>
                {% endif %}

            </form>
        </div>
    </div>
</template>


<script>
    export default {
        
    }
</script>

<style scoped>

</style>