<template>
<div class="container">
    <h1 class="display-3 text-center">Register</h1>

    <div v-if="usernameTaken" class="user-exists-alert alert alert-danger alert-dismissible fade show" role="alert">
        <strong>Username already taken!</strong> Please try a different username.
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    <RegisterForm/>
</div>
</template>
<script>
import RegisterForm from '@/components/RegisterForm.vue'
export default {
  name: "RegisterView",
  components: {
    RegisterForm
  }
}
</script>