(function(e){function t(t){for(var a,r,l=t[0],s=t[1],p=t[2],c=0,d=[];c<l.length;c++)r=l[c],Object.prototype.hasOwnProperty.call(i,r)&&i[r]&&d.push(i[r][0]),i[r]=0;for(a in s)Object.prototype.hasOwnProperty.call(s,a)&&(e[a]=s[a]);u&&u(t);while(d.length)d.shift()();return o.push.apply(o,p||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],a=!0,l=1;l<n.length;l++){var s=n[l];0!==i[s]&&(a=!1)}a&&(o.splice(t--,1),e=r(r.s=n[0]))}return e}var a={},i={app:0},o=[];function r(t){if(a[t])return a[t].exports;var n=a[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,r),n.l=!0,n.exports}r.m=e,r.c=a,r.d=function(e,t,n){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},r.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(r.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)r.d(n,a,function(t){return e[t]}.bind(null,a));return n},r.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="/";var l=window["webpackJsonp"]=window["webpackJsonp"]||[],s=l.push.bind(l);l.push=t,l=l.slice();for(var p=0;p<l.length;p++)t(l[p]);var u=s;o.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";n("85ec")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var a=n("2b0e"),i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{attrs:{id:"app"}},[a("img",{attrs:{alt:"Vue logo",src:n("cf05")}}),a("Header",{attrs:{title:"Welcome to encore-shop"}}),e.login_flag?a("p",[a("router-link",{attrs:{to:"/login"}},[e._v("login")])],1):e._e(),e.login_flag?e._e():a("p",[a("button",{on:{click:e.logout}},[e._v("logout")])]),a("router-view",{key:e.$route.fullPath}),a("Footer",{attrs:{info:"copyrighted by encore company tel:02-1111-2222"}})],1)},o=[],r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"head"},[n("h1",[e._v(e._s(e.title))])])},l=[],s={name:"Header",props:{title:String}},p=s,u=n("2877"),c=Object(u["a"])(p,r,l,!1,null,null,null),d=c.exports,m=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"footer"},[n("h1",[e._v(e._s(e.info))]),n("p",[e._v(" footer: bottom text ")])])},v=[],f={name:"Footer",props:{info:String}},_=f,g=(n("8ce8"),Object(u["a"])(_,m,v,!1,null,"0232ec90",null)),h=g.exports,y={name:"App",components:{Header:d,Footer:h},data:function(){return{login_flag:!0}},created:function(){var e=sessionStorage.getItem("login_id");this.login_flag=""==e||null==e},methods:{logout:function(){this.login_flag=!0,sessionStorage.removeItem("login_id"),sessionStorage.removeItem("type_num"),sessionStorage.removeItem("type_name"),location.href="index.html"},setFlag:function(e){this.login_flag=e}}},b=y,w=(n("034f"),Object(u["a"])(b,i,o,!1,null,null,null)),x=w.exports,$=n("8c4f"),P=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("h3",[e._v("LOGIN")]),n("div",[n("label",{attrs:{for:"id"}},[e._v("id")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.idval,expression:"idval"}],attrs:{type:"text",id:"id"},domProps:{value:e.idval},on:{input:function(t){t.target.composing||(e.idval=t.target.value)}}})]),n("div",[n("label",{attrs:{for:"pwd"}},[e._v("pwd")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.pwdval,expression:"pwdval"}],attrs:{type:"password",id:"pwd"},domProps:{value:e.pwdval},on:{input:function(t){t.target.composing||(e.pwdval=t.target.value)}}})]),n("button",{on:{click:e.loginForm}},[e._v("login")]),n("router-link",{attrs:{to:"/join"}},[e._v(" join")])],1)},j=[],S=(n("b0c0"),{name:"Login",data:function(){return{idval:"",pwdval:"",m:null}},methods:{loginForm:function(){var e=this;this.$axios.get("/shop-members/"+e.idval).then((function(t){if(t.data.result)if(e.m=t.data.data,e.m.pwd==e.pwdval){sessionStorage.setItem("login_id",e.m.id),sessionStorage.setItem("type_num",e.m.type.num),sessionStorage.setItem("type_name",e.m.type.name),e.$parent.setFlag(!1),alert("login success");var n="";if(2==e.m.type.num)n="/smain";else{if(3!=e.m.type.num)return void alert("준비되지 않음");n="/cmain"}e.$router.push(n)}else alert("pwd fail");else alert("not found id")}))}}}),O=S,N=Object(u["a"])(O,P,j,!1,null,null,null),k=N.exports,I=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("h3",[e._v("JOIN")]),n("div",[n("label",{attrs:{for:"id"}},[e._v("id")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.id,expression:"id"}],attrs:{type:"text",id:"id"},domProps:{value:e.id},on:{input:function(t){t.target.composing||(e.id=t.target.value)}}})]),n("div",[n("label",{attrs:{for:"pwd"}},[e._v("pwd")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.pwd,expression:"pwd"}],attrs:{type:"password",id:"pwd"},domProps:{value:e.pwd},on:{input:function(t){t.target.composing||(e.pwd=t.target.value)}}})]),n("div",[n("label",{attrs:{for:"name"}},[e._v("name")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.name,expression:"name"}],attrs:{type:"text",id:"name"},domProps:{value:e.name},on:{input:function(t){t.target.composing||(e.name=t.target.value)}}})]),n("div",[n("label",{attrs:{for:"email"}},[e._v("email")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.email,expression:"email"}],attrs:{type:"text",id:"email"},domProps:{value:e.email},on:{input:function(t){t.target.composing||(e.email=t.target.value)}}})]),n("div",[n("input",{directives:[{name:"model",rawName:"v-model",value:e.type,expression:"type"}],attrs:{type:"radio",name:"type",id:"type2",value:"2"},domProps:{checked:e._q(e.type,"2")},on:{change:function(t){e.type="2"}}}),n("label",{attrs:{for:"type2"}},[e._v("seller")]),n("br"),n("input",{directives:[{name:"model",rawName:"v-model",value:e.type,expression:"type"}],attrs:{type:"radio",name:"type",id:"type3",value:"3"},domProps:{checked:e._q(e.type,"3")},on:{change:function(t){e.type="3"}}}),n("label",{attrs:{for:"type3"}},[e._v("consumer")])]),n("button",{on:{click:e.joinForm}},[e._v("join")])])},E=[],M=(n("2b3d"),n("d3b7"),n("3ca3"),n("ddb0"),{name:"Join",data:function(){return{id:"",pwd:"",name:"",email:"",type:""}},methods:{joinForm:function(){var e=new URLSearchParams;e.append("id",this.id),e.append("pwd",this.pwd),e.append("name",this.name),e.append("email",this.email),e.append("type",this.type),this.$axios.post("/shop-members/",e).then((function(e){e.data.result?(alert("join success: join_id="+e.data.join_id),location.href="index.html"):alert("join fail")}))}}}),F=M,L=Object(u["a"])(F,I,E,!1,null,null,null),J=L.exports,A=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("p",[e._v("판매자("+e._s(e.id)+" / "+e._s(e.type_name)+") Menu")]),n("p",[n("router-link",{attrs:{to:"/add-product"}},[e._v("상품등록")])],1),n("p",[e._v(e._s(e.id)+"가 등록한 상품")]),n("table",{attrs:{border:"1"}},[e._m(0),e._l(e.plist,(function(t){return n("tr",{key:t.num},[n("td",[e._v(e._s(t.num))]),n("td",[e._v(e._s(t.title))]),n("td",[e._v(e._s(t.price))]),n("button",{on:{click:function(n){return e.edit(t.num)}}},[e._v("edit")]),n("button",{on:{click:function(n){return e.del(t.num)}}},[e._v("del")])])}))],2)])},C=[function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("tr",[n("th",[e._v("상품번호")]),n("th",[e._v("상품제목")]),n("th",[e._v("가격")]),n("th",[e._v("편집")])])}],H={name:"SMain",data:function(){return{id:"",type_num:"",type_name:"",plist:[]}},created:function(){var e=this;e.id=sessionStorage.getItem("login_id"),e.type_num=sessionStorage.getItem("type_num"),e.type_name=sessionStorage.getItem("type_name"),this.$axios.get("/products/"+e.id+"/members").then((function(t){200==t.status?t.data.result?e.plist=t.data.list:alert("plist fail"):alert("connect fail:"+t.status)}))},methods:{edit:function(e){this.$router.push({name:"EditProduct",params:{num:e}})},del:function(e){var t=this;this.$axios.delete("/products/"+e).then((function(e){e.data.result?(alert("삭제완료"),t.$router.push("/smain"),location.reload()):alert("삭제실패")}))}}},R=H,T=Object(u["a"])(R,A,C,!1,null,null,null),U=T.exports,q=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("h3",[e._v(e._s(e.num)+"번 상품 편집 페이지")]),n("table",[n("tr",e._l(e.files,(function(t){return n("td",{key:t},[e._v(e._s(t)),n("img",{staticStyle:{width:"100px",height:"100px"},attrs:{src:"f"}})])})),0)]),n("div",[n("label",{attrs:{for:"title"}},[e._v("title")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.p.title,expression:"p.title"}],attrs:{type:"text",id:"title"},domProps:{value:e.p.title},on:{input:function(t){t.target.composing||e.$set(e.p,"title",t.target.value)}}})]),n("div",[n("label",{attrs:{for:"content"}},[e._v("content")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.p.content,expression:"p.content"}],attrs:{type:"text",id:"content"},domProps:{value:e.p.content},on:{input:function(t){t.target.composing||e.$set(e.p,"content",t.target.value)}}})]),n("div",[n("label",{attrs:{for:"price"}},[e._v("price")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.p.price,expression:"p.price"}],attrs:{type:"number",id:"price"},domProps:{value:e.p.price},on:{input:function(t){t.target.composing||e.$set(e.p,"price",t.target.value)}}})]),n("div",[n("label",{attrs:{for:"amount"}},[e._v("amount")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.p.amount,expression:"p.amount"}],attrs:{type:"number",id:"amount"},domProps:{value:e.p.amount},on:{input:function(t){t.target.composing||e.$set(e.p,"amount",t.target.value)}}})]),n("p",[n("label",{attrs:{for:"cate"}},[e._v("상품 카테고리")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.p.cate.name,expression:"p.cate.name"}],attrs:{type:"text",id:"cate",readonly:""},domProps:{value:e.p.cate.name},on:{input:function(t){t.target.composing||e.$set(e.p.cate,"name",t.target.value)}}})]),n("button",{on:{click:e.save}},[e._v("수정")])])},G=[],V={name:"EditProduct",data:function(){return{num:this.$route.params.num,p:null,files:[]}},created:function(){var e=this;this.$axios.get("/products/"+e.num).then((function(t){if(200==t.status){var n=t.data;if(n.result){e.p=n.p;var a=0;for(var i in n)"p"!=i&&"result"!=i&&(e.files[a++]=n[i])}else alert("plist fail")}else alert("connect fail:"+t.status)}))},methods:{save:function(){var e=this,t=new URLSearchParams;t.append("num",e.p.num),t.append("title",e.p.title),t.append("content",e.p.content),t.append("price",e.p.price),t.append("amount",e.p.amount),t.append("cate",e.p.cate.num),t.append("seller",e.p.seller.id),this.$axios.put("/products/",t).then((function(t){if(200==t.status){var n=t.data;n.result?(alert("edit success"),e.$router.push("/smain")):alert("edit fail")}else alert("connect fail:"+t.status)}))}}},W=V,z=Object(u["a"])(W,q,G,!1,null,null,null),B=z.exports,D=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("h3",[e._v("상품등록")]),n("div",[n("label",{attrs:{for:"title"}},[e._v("title")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.title,expression:"title"}],attrs:{type:"text",id:"title"},domProps:{value:e.title},on:{input:function(t){t.target.composing||(e.title=t.target.value)}}})]),n("div",[n("label",{attrs:{for:"content"}},[e._v("content")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.content,expression:"content"}],attrs:{type:"text",id:"content"},domProps:{value:e.content},on:{input:function(t){t.target.composing||(e.content=t.target.value)}}})]),n("div",[n("label",{attrs:{for:"price"}},[e._v("price")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.price,expression:"price"}],attrs:{type:"number",id:"price"},domProps:{value:e.price},on:{input:function(t){t.target.composing||(e.price=t.target.value)}}})]),n("div",[n("label",{attrs:{for:"amount"}},[e._v("amount")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.amount,expression:"amount"}],attrs:{type:"number",id:"amount"},domProps:{value:e.amount},on:{input:function(t){t.target.composing||(e.amount=t.target.value)}}})]),n("div",[n("label",{attrs:{for:"file1"}},[e._v("상품사진")]),n("input",{ref:"file1",attrs:{type:"file"}}),n("input",{ref:"file2",attrs:{type:"file"}}),n("input",{ref:"file3",attrs:{type:"file"}}),n("input",{ref:"file4",attrs:{type:"file"}})]),n("p",[n("label",{attrs:{for:"cate"}},[e._v("카테고리 선택")]),n("select",{directives:[{name:"model",rawName:"v-model",value:e.cate,expression:"cate"}],attrs:{id:"cate"},on:{change:function(t){var n=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.cate=t.target.multiple?n:n[0]}}},e._l(e.cates,(function(t){return n("option",{key:t.num,domProps:{value:t.num}},[e._v(e._s(t.name))])})),0)]),n("button",{on:{click:e.add}},[e._v("등록")])])},K=[],Q={name:"AddProduct",data:function(){return{cates:[],title:"",content:"",price:0,amount:0,cate:""}},created:function(){var e=this;this.$axios.get("/cates/").then((function(t){200==t.status?t.data.result?e.cates=t.data.list:alert("plist fail"):alert("connect fail:"+t.status)}))},methods:{add:function(){var e=this,t=new URLSearchParams;t.append("title",e.title),t.append("content",e.content),t.append("seller",sessionStorage.getItem("login_id")),t.append("price",e.price),t.append("amount",e.amount),t.append("cate",e.cate),null!=this.$refs.file1.files[0]&&t.append("file1",this.$refs.file1.files[0]),null!=this.$refs.file2.files[0]&&t.append("file2",this.$refs.file2.files[0]),null!=this.$refs.file3.files[0]&&t.append("file3",this.$refs.file3.files[0]),null!=this.$refs.file4.files[0]&&t.append("file4",this.$refs.file4.files[0]),this.$axios.post("/products/",t).then((function(t){t.data.result?(alert("등록완료"),e.$router.push("/smain")):alert("등록실패")}))}}},X=Q,Y=Object(u["a"])(X,D,K,!1,null,null,null),Z=Y.exports,ee=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("p",[e._v("구매자 Menu")]),n("p",[e._v(e._s(e.id)+" / "+e._s(e.type_num)+" / "+e._s(e.type_name))])])},te=[],ne={name:"CMain",data:function(){return{id:"",type_num:"",type_name:"",plist:[]}},created:function(){this.id=sessionStorage.getItem("login_id"),this.type_num=sessionStorage.getItem("type_num"),this.type_name=sessionStorage.getItem("type_name"),alert(this.id+"/"+this.type_name)},methods:{}},ae=ne,ie=Object(u["a"])(ae,ee,te,!1,null,null,null),oe=ie.exports;a["a"].use($["a"]);var re=new $["a"]({mode:"history",routes:[{path:"/login",name:"Login",component:k},{path:"/join",name:"Join",component:J},{path:"/smain",name:"SMain",component:U},{path:"/edit-product",name:"EditProduct",component:B},{path:"/add-product",name:"AddProduct",component:Z},{path:"/cmain",name:"CMain",component:oe}]}),le=n("bc3a"),se=n.n(le);a["a"].config.productionTip=!1,a["a"].prototype.$axios=se.a,new a["a"]({router:re,render:function(e){return e(x)}}).$mount("#app")},"5ad6":function(e,t,n){},"85ec":function(e,t,n){},"8ce8":function(e,t,n){"use strict";n("5ad6")},cf05:function(e,t,n){e.exports=n.p+"img/logo.82b9c7a5.png"}});
//# sourceMappingURL=app.87e23dd0.js.map