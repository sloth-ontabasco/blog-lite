<template lang="en">
    <div class="container">
        <div class="row">
            <div class="col col-sm">
                <img src="@/assets/splash.jpg" class="img-fluid">
            </div>
            <LoginForm/>
        </div>
    </div>
</template>
<script>
import LoginForm from "@/components/LoginForm.vue";
export default {
  name: "LoginView",
  components: { LoginForm },
};
</script>
<style lang=""></style>
