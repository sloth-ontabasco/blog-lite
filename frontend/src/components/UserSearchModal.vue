<template>
    <!--Modal for search-->
    <div class="modal fade" tabindex="-1" role="dialog" id="make-search">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Search For Users</h5>
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
                    <div class="col-md input-group flex-nowrap">
                        <span class="input-group-text" id="addon-wrapping"
                            >@</span
                        >
                        <div class="form-floating align-items-center">
                            <input
                                v-model="searchText"
                                @keyup="handleKeyPress"
                                type="text"
                                class="form-control"
                                id="floatingInputGroup1"
                                placeholder="Username"
                                aria-describedby="addon-wrapping"
                            />
                            <label for="floatingInputGroup1">Username</label>
                        </div>
                    </div>
                    <UserSearchResult v-if="noUsersFound == false" v-for="user in searchResults" :user="user"></UserSearchResult>
                    <div
                        v-if="noUsersFound"
                        id="user-display"
                        class="container container-fluid"
                    >
                        <div class="d-flex justify-content-center mt-2">
                            <p>Could not find any users with that username</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!--Modal for search-->
</template>

<script>
    import { searchUsers, getImageURL } from '@/api';
    import  UserSearchResult  from '@/components/UserSearchResult.vue'
    export default {
        name: "UserSearchModal",
        data() {
            return {
                searchText: "",
                noUsersFound: null,
                searchResults: []
            }
        },
        methods: {
            handleKeyPress() {
                console.log("Handling key press")
                searchUsers(this.$store.state.token, this.searchText)
                    .then((data) => {
                        this.noUsersFound = false;
                        this.searchResults = data;
                    })
                    .catch((e) => (this.noUsersFound = true));
            },

            resolvePfp(id) {
                const pfp = {url:null};
                getImageURL("profile_picutes/" + id + ".png")
                .then(data => {pfp.url = data})
                .catch(e => {
                    pfp.url = this.$store.state.defaultPfpURL
                })
                return pfp.url;
            }
        },
        components: {
            UserSearchResult
        }
    };
</script>
