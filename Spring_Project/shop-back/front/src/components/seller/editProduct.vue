<template>
<div>
  <h3>{{num}}번 상품 편집 페이지</h3>
  <table>
    <tr>
      <td :key="f" v-for="f in files"><img :src="f" style="width:200px;height:200px"></td>
    </tr>
  </table>
  <div><label for="title">title</label><input type="text" id="title" v-model="p.title" /></div>
  <div><label for="content">content</label><input type="text" id="content" v-model="p.content" /></div>
  <div><label for="price">price</label><input type="number" id="price" v-model="p.price" /></div>
  <div><label for="amount">amount</label><input type="number" id="amount" v-model="p.amount" /></div>
  <p><label for="cate">상품 카테고리</label><input type="text" id="cate" v-model="p.cate.name" readonly /></p>
  <button v-on:click="save">수정</button>
</div>
</template>
<script>
export default {
  name: 'EditProduct',
  data() {
    return {
      num: this.$route.params.num,
      p: null,
      files: []
    };
  },
  created: function() {
    const self = this;
    this.$axios.get('/products/' + self.num)
      .then(function(response) { //response: 응답객체
        if (response.status == 200) { //웹 응답이 정상
          var data = response.data
          if (data.result) { //백단의 처리 결과가 정상
            self.p = data.p;
            var cnt = 0;

            for (var key in data) {
              if (key != 'p' && key != 'result') {
                self.files[cnt++] = data[key];
              }
            }

          } else {
            alert('plist fail')
          }
        } else {
          alert('connect fail:' + response.status);
        }
      })
  },
  methods: {
    save: function() {
      const self = this;
      const form = new URLSearchParams(); // URLSearchParams: 읽거나 수정할때 사용 / 폼파람 객체.
      form.append('num', self.p.num)
      form.append('title', self.p.title)
      form.append('content', self.p.content)
      form.append('price', self.p.price)
      form.append('amount', self.p.amount)
      form.append('cate', self.p.cate.num)
      form.append('seller', self.p.seller.id)
      this.$axios.put('/products/', form)
        .then(function(response) { //response: 응답객체
          if (response.status == 200) { //웹 응답이 정상
            var data = response.data
            if (data.result) { //백단의 처리 결과가 정상
              alert('edit success')
              self.$router.push('/smain')
            } else {
              alert('edit fail')
            }
          } else {
            alert('connect fail:' + response.status);
          }
        })
    }
  }
}
</script>
