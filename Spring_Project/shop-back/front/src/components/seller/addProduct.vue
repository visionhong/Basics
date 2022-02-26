<template>
  <div>
    <h3>상품등록폼</h3>
    <div>
      <label for="title">title</label>
      <input type="text" id="title" v-model="title" />
    </div>
    <div>
      <label for="content">content</label>
      <input type="text" id="content" v-model="content" />
    </div>
    <div>
      <label for="price">price</label>
      <input type="number" id="price" v-model="price" />
    </div>
    <div>
      <label for="amount">amount</label>
      <input type="number" id="amount" v-model="amount" />
    </div>
    <div>
      <label for="file1">상품사진</label><br />
      <!-- f값이 있으면 화면에 뿌려주기 -->
      <input type="file" ref="file1" @change="viewImg(1)" />
      <img v-if="f1" :src="f1" style="width: 50px; height: 50px" /><br />
      <input type="file" ref="file2" @change="viewImg(2)" />
      <img v-if="f2" :src="f2" style="width: 50px; height: 50px" /><br />
      <input type="file" ref="file3" @change="viewImg(3)" />
      <img v-if="f3" :src="f3" style="width: 50px; height: 50px" /><br />
      <input type="file" ref="file4" @change="viewImg(4)" />
      <img v-if="f4" :src="f4" style="width: 50px; height: 50px" /><br />
    </div>
    <p>
      <label for="cate">카테고리 선택</label>
      <select id="cate" v-model="cate">
        <option :key="c" v-for="c in cates" v-bind:value="c.num">
          {{ c.name }}
        </option>
      </select>
    </p>
    <button v-on:click="add">등록</button>
  </div>
</template>
<script>
export default {
  name: "AddProduct",
  data() {
    //반응형. 값이 갱신되면 화면도 갱신
    return {
      cates: [],
      title: "",
      content: "",
      price: 0,
      amount: 0,
      cate: "",
      f1: null,
      f2: null,
      f3: null,
      f4: null,
    };
  },
  created: function () {
    const self = this;
    this.$axios.get("/cates/").then(function (response) {
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
  methods: {
    viewImg: function (num) {
      switch (num) {
        case 1:
          this.f1 = URL.createObjectURL(this.$refs.file1.files[0]);
          break;
        case 2:
          this.f2 = URL.createObjectURL(this.$refs.file2.files[0]);
          break;
        case 3:
          this.f3 = URL.createObjectURL(this.$refs.file3.files[0]);
          break;
        case 4:
          this.f4 = URL.createObjectURL(this.$refs.file4.files[0]);
          break;
      }
    },

    add: function () {
      //title, content, seller, price, amount, cate, file1~4
      const self = this;
      const form = new FormData(); //FormData(): 새롭게 추가할때 사용 / 폼파람 객체.
      form.append("title", self.title);
      form.append("content", self.content);
      form.append("seller", sessionStorage.getItem("login_id"));
      form.append("price", self.price);
      form.append("amount", self.amount);
      form.append("cate", self.cate);
      if (self.$refs.file1.files[0] != null)
        form.append("file1", self.$refs.file1.files[0]);
      if (self.$refs.file2.files[0] != null)
        form.append("file2", self.$refs.file2.files[0]);
      if (self.$refs.file3.files[0] != null)
        form.append("file3", self.$refs.file3.files[0]);
      if (self.$refs.file4.files[0] != null)
        form.append("file4", self.$refs.file4.files[0]);

      self.$axios
        .post("/products/", form, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(function (response) {
          //response: 응답객체
          //alert(response.status);
          if (response.data.result) {
            alert("등록완료");
            self.$router.push("/smain");
          } else {
            alert("등록실패");
          }
        });
    },
  },
};
</script>
