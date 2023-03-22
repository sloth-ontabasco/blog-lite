<template>
  <nav>
    <router-link to="/home">Home</router-link> |
    <router-link to="/about">About</router-link>  |
    <router-link to="/login">Login</router-link> |
    <router-link to="/register">Register</router-link> 
  </nav>
  <router-view/>
</template>
<script>
export default {
  mounted() {
    if(localStorage.token) {
      this.$store.state.jwt = localStorage.token;
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.iconbutton {
    width: 60px;
    height: 60px;
    border-radius: 100%;
    background: #FF4F79;
}

.button {
    width: 80px;
    height: 80px;
    background: #000000;
    position: fixed;
    bottom: 60px;
    right: 60px;
}

.iconbutton i {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: white;
}

.pfp {
    height: 50px;
    width: 50px;
    border-radius: 50%;
}

.comment-pfp {
    border-radius: 50%;
    height: 25px;
    width: 25px;
}
</style>
