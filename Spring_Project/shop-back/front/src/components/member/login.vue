<template>
<div>
  <h3>LOGIN</h3>
  <div>
    <label for="id">id</label>
    <input type="text" id="id" v-model="idval" />
  </div>
  <div>
    <label for="pwd">pwd</label>
    <input type="password" id="pwd" v-model="pwdval" />
  </div>
  <button v-on:click="loginForm">login</button>
  <router-link to="/join"> join</router-link>
</div>
</template>
<script>
export default {
  name: 'Login',
  data() {
    return {
      idval: '',
      pwdval: '',
      m: null
    };
  },
  methods: {
    loginForm: function() {
      const self = this
      this.$axios.get('/shop-members/' + self.idval)
        .then(function(response) { //response: 응답객체
          if (response.data.result) {
            self.m = response.data.data;
            if (self.m.pwd == self.pwdval) {
              sessionStorage.setItem("login_id", self.m.id);
              sessionStorage.setItem("type_num", self.m.type.num);
              sessionStorage.setItem("type_name", self.m.type.name);
              self.$parent.setFlag(false) //부모 컴포넌트 메서드 호출
              alert('login success')
              var path = '';
              if (self.m.type.num == 2) {
                path = '/smain'
              } else if (self.m.type.num == 3) {
                path = '/omain'
              } else {
                alert("준비되지 않음")
                return
              }
              self.$router.push(path);
            } else {
              alert('pwd fail')
            }
          } else {
            alert('not found id')
          }
        })
    }
  }
}
</script>
