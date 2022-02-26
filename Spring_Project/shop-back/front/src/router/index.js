/**
 *
 */
import Vue from "vue";
import VueRouter from "vue-router";
import Login from "@/components/member/login.vue";
import Join from "@/components/member/join.vue";
import SMain from "@/components/seller/sellerMain.vue";
import EditProduct from "@/components/seller/editProduct.vue";
import AddProduct from "@/components/seller/addProduct.vue";
import OMain from "@/components/orders/orderMain.vue";
import DetailProduct from "@/components/orders/detailProduct.vue";
import OrderList from "@/components/orders/orderList.vue";



Vue.use(VueRouter); // 뷰 어플리케이션에 라우터 플러그인을 추가한다.

// 라우터 객체를 생성
export default new VueRouter({
  mode: "history",
  routes: [{
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/join",
    name: "Join",
    component: Join
  },
  {
    path: "/smain",
    name: "SMain",
    component: SMain
  },
  {
    path: "/edit-product",
    name: "EditProduct",
    component: EditProduct
  },
  {
    path: "/add-product",
    name: "AddProduct",
    component: AddProduct
  },
  {
    path: "/omain",
    name: "OMain",
    component: OMain
  },
  {
    path: "/detail-product",
    name: "DetailProduct",
    component: DetailProduct
  },
  {
    path: "/olist",
    name: "OrderList",
    component: OrderList
  }]
});
