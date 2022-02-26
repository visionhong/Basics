<template>
<div>
  <h3>상품 상세 페이지</h3>
  <router-link to="/omain">목록으로 돌아가기</router-link><br>
  <table>
    <tr>
      <th>상품 타이틀</th>
      <td>{{p.title}}</td>
    </tr>
    <tr>
      <th>상품 이미지</th>
      <td>
        <table>
          <tr>
            <td :key="f" v-for="f in files">
              <img :src="f" style="width:100px;height:100px">
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <th>상품 가격</th>
      <td>{{p.price}}</td>
    </tr>
    <tr>
      <th>주문수량</th>
      <td><input type="number" v-model="amount" @change="check" /></td>
    </tr>
    <tr>
      <th>결제금액</th>
      <td>{{payment}}</td>
    </tr>
    <tr>
      <th>주문</th>
      <td>
        <button v-on:click="order1">장바구니</button>
        <button v-on:click="order2">즉시결제</button>
      </td>
    </tr>
    <tr>
      <th>상품 설명</th>
      <td>{{p.content}}</td>
    </tr>
  </table>
</div>
</template>
<script>
//상품번호(prod), 구매자(consumer), 수량(amount), 결제금액(payment)
export default {
  name: 'DetailProduct',
  data() {
    return {
      num: this.$route.params.num,
      p: null,
      files: [],
      amount: 0,
      payment: 0,
    };
  },
  watch: {
    payment: function() {
      return this.payment
    }
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
    check: function() {
      
      this.payment = this.p.price * this.amount
     
    },
    order1: function() {
      const self = this;
      const form = new FormData(); //FormData(): 새롭게 추가할때 사용 / 폼파람 객체.

      form.append('prod', self.p.num)
      form.append('consumer', sessionStorage.getItem("login_id"))
      form.append('amount', self.amount)
      form.append('payment', self.payment)
      form.append('pay', false)

      self.$axios.post('/orders/', form)
        .then(function(response) { //response: 응답객체
          //alert(response.status);
          if (response.data.result) {
            var data = response.data
            if (data.result){
              alert('장바구니 등록완료')
              self.$router.push('/omain');
            }else {
            alert('장바구니 등록실패')
            }
          }else {
            alert('connecy fail:'+response.status)
          }
        })
    },
    order2: function(){
      const self = this;
      const form = new FormData(); //FormData(): 새롭게 추가할때 사용 / 폼파람 객체.

      form.append('prod', self.p.num)
      form.append('consumer', sessionStorage.getItem("login_id"))
      form.append('amount', self.amount)
      form.append('payment', self.payment)
      form.append('pay', true)

      self.$axios.post('/orders/', form)
        .then(function(response) { //response: 응답객체
          //alert(response.status);
          if (response.data.result) {
            var data = response.data
            if (data.result){
              alert('결제완료')
              self.$router.push('/omain');
            }else {
            alert('결제실패')
            }
          }else {
            alert('connecy fail:'+response.status)
          }
        })
    }

  }

}
</script>
