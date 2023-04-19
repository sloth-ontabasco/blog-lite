<template>
        <div class="row mt-5">
            <div class="col col-2">
                <img
                    :src="pfpURL"
                    height="130px"
                    width="130px"
                    style="border-radius: 50%"
                />
            </div>
            <div class="col col-4 d-flex flex-column align-items-stretch">
                <h1 class="h1 mt-3">{{ user.name }}</h1>
                <h5 class="text-muted">@{{ user.username }}</h5>
            </div>
            <!-- <div class="col col-3 d-flex align-items-end vstack"> -->
                <button
                    type="button"
                    class="m-4 btn btn-outline-dark col col-2"
                    data-bs-toggle="modal"
                    data-bs-target="#show-followed"
                    id="followers-btn"
                >
                    {{ user.followed.length }} Following
                </button>
                <button
                    type="button"
                    class="m-4 btn btn-outline-dark col col-2"
                    data-bs-toggle="modal"
                    href="#show-followers"
                    id="followed-btn"
                >
                    {{ user.followers.length }} Followers
                </button>

            <!-- </div> -->
            <div
                class="col col-3 d-flex flex-column justify-content-center user-buttons"
            >
                <button
                    v-if="user.id == $store.getters.userID"
                    class="btn btn-outline-dark"
                    data-bs-toggle="modal"
                    data-bs-target="#edit-user"
                >
                    <i class="fa fa-solid fa-pen-to-square"></i> Edit Profile
                </button>
            </div>
        </div>
</template>

<script>
import { getImageURL } from '@/api';
export default {
    name: 'ProfileHeader',
    props: {
        user: {
            type: Object,
            default: {}
        }
    },
    data() {
        return {
            pfpURL: null
        }
    },
    mounted() {
        getImageURL("profile_pictures/" + this.user.id + ".png")
        .then((url) => (this.pfpURL = url))
        .catch((e) => {this.pfpURL = this.$store.state.defaultPfpURL; console.log(this.$store.state.defaultPfpURL) });
    }
}
</script>