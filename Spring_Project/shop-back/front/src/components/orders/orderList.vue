<template>
  <div>
    <h3>내 주문목록</h3>
    {{ info }}<br />
    <router-link to="/omain">메인으로</router-link><br />
    <table border="1">
      <tr>
        <th>상품명</th>
        <th>주문일</th>
        <th>단가</th>
        <th>수량</th>
        <th>결제금액</th>
        <th>결제유무</th>
      </tr>
      <tr v-for="o in olist" :key="o.num">
        <td>{{ o.prod.title }}</td>
        <td>{{ o.order_date }}</td>
        <td>{{ o.prod.price }}</td>
        <td>{{ o.amount }}</td>
        <td>{{ o.payment }}</td>
        <td>{{ o.pay }}</td>
      </tr>
    </table>
  </div>
</template>
<script>
export default {
  name: "OrderList",
  data() {
    //컴포넌트에서 사용하는 값 저장
    return {
      olist: [],
      info: "",
    };
  },
  created: function () {
    var id = sessionStorage.getItem("login_id");
    const self = this;
    self.$axios.get("/orders/" + id + "/members").then(function (response) {
      //response: 응답객체
      if (response.status == 200) {
        //웹 응답이 정상
        var data = response.data;
        if (data.result) {
          //백단의 처리 결과가 정상
          self.olist = data.list;
          if (self.olist.length == 0) {
            self.info = "구매 목록 없음";
          }
        } else {
          alert("olist fail");
        }
      } else {
        alert("connect fail:" + response.status);
      }
    });
  },
};
</script>
