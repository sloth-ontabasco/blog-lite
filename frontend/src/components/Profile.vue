<template>
    <div class="container">
        <ProfileHeader v-if="user" :user="user"/>
        <hr />
        <ProfilePosts v-if="user" :user="user"/>
    </div>
</template>
<script>
import ProfileHeader from './profile/ProfileHeader.vue';
import ProfilePosts from './profile/ProfilePosts.vue';
export default {
    name: 'Profile',
    props: {
        user: Object
    },
    mounted() {
        console.log("In Profile mounted",this.user)
    },
    components: {
        ProfileHeader,
        ProfilePosts
    }
}
</script>