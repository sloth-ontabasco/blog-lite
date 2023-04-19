<template>
  <form action="/register" method="post" enctype="multipart/form-data">
    <div class="form-group">
      <div class="preview">
        <img id="file-ip-1-preview" />
      </div>
      <label for="file-upload">Upload Profile Picture</label><br />
      <input
        type="file"
        id="file-upload"
        name="file-upload"
        accept="image/*"
        onchange="showPreview(event);"
      />
    </div>
    <div class="form-group">
      <label for="username">Username</label>
      <input
        v-model="username"
        type="text"
        class="form-control"
        name="username"
        id="username"
        placeholder="Enter username"
        required
      />
    </div>

    <div class="form-group">
      <label for="password">Password</label>
      <input
        v-model="password"
        type="password"
        class="form-control"
        name="password"
        id="password"
        placeholder="Password"
        required
      />
    </div>

    <div class="form-group">
      <label for="name">Name</label>
      <input
        v-model="name"
        type="text"
        class="form-control"
        name="name"
        id="name"
        placeholder="Name"
        required
      />
    </div>

    <button @click.prevent="registerUser" class="btn btn-primary">
      Submit
    </button>
  </form>
</template>
<script>
import { register } from '@/api/index.js'
export default {
    name: 'RegisterForm',
    data() {
        return {
            username: "",
            password: "",
            name: "",
            usernameTaken: false
        }
    },
    methods: {
        async registerUser() {
            let res = await register({
                username: this.username,
                password: this.password,
                name: this.name
            })
        }
    }
}
</script>
