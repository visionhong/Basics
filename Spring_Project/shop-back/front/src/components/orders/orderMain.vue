<template>
  <div>
    <h3>
      구매자({{ id }} / {{ type_name }}) Menu
      <router-link to="/olist">내 구매목록</router-link>
    </h3>
    <h3>{{ title }}</h3>
    <select v-model="select_type" @change="searchby">
      <option value="1">전체 검색</option>
      <option value="2">카테고리 검색</option>
      <option value="3">판매자로 검색</option>
    </select>
    <span v-if="select_type === '1'"> </span>
    <span v-else-if="select_type === '2'">
      <label for="cate">카테고리 선택</label>
      <select id="cate" v-model="cate" @change="searchbycate">
        <option :key="c" v-for="c in cates" v-bind:value="c.num">
          {{ c.name }}
        </option>
      </select>
    </span>

    <span v-else-if="select_type === '3'">
      판매자 id:<input type="text" v-model="seller" />
      <button v-on:click="searchbyseller">검색</button>
    </span>
    <br />
    <table border="1">
      <tr>
        <th>상품번호</th>
        <th>상품제목</th>
        <th>가격</th>
        <th>판매자</th>
      </tr>
      <tr v-for="p in plist" :key="p.num">
        <td>{{ p.num }}</td>
        <td>
          <router-link
            :to="{ name: 'DetailProduct', params: { num: p.num } }"
            >{{ p.title }}</router-link
          >
        </td>
        <td>{{ p.price }}</td>
        <td>{{ p.seller.id }}</td>
      </tr>
    </table>
  </div>
</template>
<script>
export default {
  name: "OrderMain",
  data() {
    return {
      id: "",
      type_num: "",
      type_name: "",
      plist: [],
      title: "",
      select_type: 1,
      cates: [],
      cate: 0,
      seller: "",
    };
  },
  created: function () {
    this.getAllProduct(); //첫화면 전체목록
  },
  methods: {
    searchby: function () {
      switch (this.select_type) {
        case "1":
          this.getAllProduct();
          break;
        case "2":
          this.getCates();
          break;
        case "3":
          break;
      }
    },

    getCates: function () {
      const self = this;
      self.$axios.get("/cates/").then(function (response) {
        if (response.status == 200) {
          if (response.data.result) {
            self.cates = response.data.list;
          } else {
            alert("plist fail");
          }
        } else {
          alert("connect fail:" + response.status);
        }
      });
    },
    getAllProduct: function () {
      const self = this;
      self.id = sessionStorage.getItem("login_id");
      self.type_num = sessionStorage.getItem("type_num");
      self.type_name = sessionStorage.getItem("type_name");
      self.$axios.get("/products/").then(function (response) {
        //response: 응답객체
        if (response.status == 200) {
          //웹 응답이 정상
          var data = response.data;
          if (data.result) {
            //백단의 처리 결과가 정상
            self.plist = data.list;
            self.title = "상품전체목록";
          } else {
            alert("plist fail");
          }
        } else {
          alert("connect fail:" + response.status);
        }
      });
    },
    searchbycate: function () {
      const self = this;
      self.$axios
        .get("/products/" + self.cate + "/cates")
        .then(function (response) {
          //response: 응답객체
          if (response.status == 200) {
            //웹 응답이 정상
            var data = response.data;
            if (data.result) {
              //백단의 처리 결과가 정상
              self.plist = data.list;
              if (self.plist.length == 0) {
                self.title = "카테고리에 등록된 상품 없음";
              } else {
                var name = self.plist[0].cate.name;
                self.title = name + " 카테고리 상품 목록";
              }
            } else {
              alert("plist fail");
            }
          } else {
            alert("connect fail:" + response.status);
          }
        });
    },
    searchbyseller: function () {
      const self = this;
      self.$axios
        .get("/products/" + self.seller + "/members")
        .then(function (response) {
          //response: 응답객체
          if (response.status == 200) {
            //웹 응답이 정상
            var data = response.data;
            if (data.result) {
              //백단의 처리 결과가 정상
              self.plist = data.list;
              if (self.plist.length == 0) {
                self.title = self.seller + " 판매자로 등록된 상품 없음";
              } else {
                self.title = self.seller + " 판매자로 등록된 상품";
              }
            } else {
              alert("plist fail");
            }
          } else {
            alert("connect fail:" + response.status);
          }
        });
    },
  },
};
</script>
