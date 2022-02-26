<template>
<div>
  <h3>JOIN</h3>
  <div><label for="id">id</label><input type="text" id="id" v-model="id" /></div>
  <div><label for="pwd">pwd</label><input type="password" id="pwd" v-model="pwd" /></div>
  <div><label for="name">name</label><input type="text" id="name" v-model="name" /></div>
  <div><label for="email">email</label><input type="text" id="email" v-model="email" /></div>
  <div><input type="radio" name="type" id="type2" value="2" v-model="type"><label for="type2">seller</label><br>
    <input type="radio" name="type" id="type3" value="3" v-model="type"><label for="type3">consumer</label>
  </div>
  <button v-on:click="joinForm">join</button>
</div>
</template>

<script>
export default {
  name: 'Join',
  data() { //컴포넌트에서 사용하는 값 저장
    return {
      id: '',
      pwd: '',
      name: '',
      email: '',
      type: ''
    }
  },
  methods: { //함수 등록
    joinForm: function() {
      const form = new URLSearchParams(); //폼파람 객체.
      form.append('id', this.id)
      form.append('pwd', this.pwd)
      form.append('name', this.name)
      form.append('email', this.email)
      form.append('type', this.type)
      this.$axios.post('/shop-members/', form)
        .then(function(response) { //response: 응답객체
          //alert(response.status);
          if (response.data.result) {
            alert('join success: join_id=' + response.data.join_id)
            location.href = "index.html"
          } else {
            alert('join fail')
          }
        })
    },
  }
}
</script>
