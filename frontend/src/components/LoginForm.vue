<template lang="en">
        <div class="col-sm">
            <h1 class="display-3 text-center">Login</h1>
            <form>
                <div class="form-group">
                    <label for="username">Username</label>
                    <input class="form-control" id="username" type="text" v-model="username" placeholder="Your Username">
                </div>

                <div class="form-group">
                    <label for="password">Password</label>
                    <input class="form-control" id="password" type="text" v-model="password" placeholder="Password">
                </div>

                <div class="form-check">
                    <input type="checkbox" class="form-check-input" id="remember">
                    <label class="form-check-label" for="remember">Remember me</label>
                </div>

                <button  @click.prevent="loginUser" class="btn btn-primary">Submit</button>
            </form>
            <p class="text-center" >Don't have an account?
                <a href="/register">register!</a>
            </p>
        </div>
</template>
<script>
export default {
    name: 'LoginForm',
    data() {
        return {
            errorMsg: "",
            username:"",
            password:"",
            remember:false
        }
    },
    methods: {
        async loginUser () {
            const res = await this.$store.dispatch('login',{username:this.username,password:this.password})
            console.log("logging in")
            this.$router.push("/home")
            // res = await fetch("http://127.0.0.1:8081/login",{
                // method: "POST",
            //     body: {
            //         username: this.username,
            //         password: this.password
            //     }
            // })
            // console.log(await res.json())

        } 
    },
    //TODO handle failed login
};

</script>
<style lang=""></style>
