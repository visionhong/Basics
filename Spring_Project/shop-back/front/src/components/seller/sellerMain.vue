<template>
<div>
  <p>판매자({{id}} / {{type_name}}) Menu</p>
  <p>
    <router-link to="/add-product">상품등록</router-link>
  </p>
  <p>{{id}}가 등록한 상품</p>
  <table border="1">
    <tr>
      <th>상품번호</th>
      <th>상품제목</th>
      <th>가격</th>
      <th>편집</th>
    </tr>
    <tr v-for="p in plist" :key="p.num">
      <td>{{p.num}}</td>
      <td>{{p.title}}</td>
      <td>{{p.price}}</td>
      <button v-on:click="edit(p.num)">edit</button><button v-on:click="del(p.num)">del</button>
    </tr>
  </table>
</div>
</template>
<script>
export default {
  name: 'SMain',
  data() {
    return {
      id: '',
      type_num: '',
      type_name: '',
      plist: [],
    };
  },
  created: function() {
    const self = this;
    self.id = sessionStorage.getItem("login_id");
    self.type_num = sessionStorage.getItem("type_num");
    self.type_name = sessionStorage.getItem("type_name");
    this.$axios.get('/products/' + self.id + '/members') //판매자 self.id로 등록된 상품들 검색
      .then(function(response) { //response: 응답객체
        if (response.status == 200) { //웹 응답이 정상
          if (response.data.result) { //백단의 처리 결과가 정상
            self.plist = response.data.list;
          } else {
            alert('plist fail')
          }
        } else {
          alert('connect fail:' + response.status);
        }
      })
  },
  methods: {
    edit: function(num) {
      this.$router.push({
        name: 'EditProduct',
        params: {
          num: num
        }
      }); //path로 params 가져가면 안됨.
    },
    del: function(num) {
      this.$axios.delete('/products/' + num)
        .then(function(response) { //response: 응답객체
          //alert(response.status);
          if (response.data.result) {
            alert('삭제완료')
            location.reload()
          } else {
            alert('삭제실패')
          }
        })
    }
  }
}
</script>
