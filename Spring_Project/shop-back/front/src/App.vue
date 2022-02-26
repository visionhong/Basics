<template>
<div id="app">
  <img alt="Vue logo" src="./assets/logo.png">
  <Header title="Welcome to encore-shop" />
  <p v-if="login_flag">
    <router-link to="/login">login</router-link>
  </p>
  <p v-if="!login_flag">
    <button v-on:click="logout">logout</button>
  </p>
  <router-view :key="$route.fullPath" />
  <Footer info="copyrighted by encore company tel:02-1111-2222" />
</div>
</template>

<script>
import Header from './components/header.vue'
import Footer from './components/footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  },
  data() {
    return {
      login_flag: true
    }
  },
  created: function() {
    var xx = sessionStorage.getItem("login_id");
		if (xx == '' || xx == null) {
			this.login_flag = true;
		} else {
			this.login_flag = false;
		}
  },
  methods: {
    logout: function() {
      this.login_flag = true;
      sessionStorage.removeItem("login_id");
      sessionStorage.removeItem("type_num");
      sessionStorage.removeItem("type_name");
      location.href = 'index.html'
    },
    setFlag: function(f){
      this.login_flag = f
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
  margin-top: 60px;
}
table{
  margin:auto;
}
</style>
