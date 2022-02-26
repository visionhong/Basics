<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<!-- css에서 요소 선택 방법 -->
<!-- 1. 태그명 -->
<!-- 2. 클래스명 -->
<!-- 3. id명 -->
<style type="text/css">
th{
	background-color:pink;
	color:red;
}

.c1{
	background-color:yellow;
	color:blue;
}

#test{
	background-color:orange;
	color:green;
}
input[type=password]{
	background-color:gray;
}

td{
	border:2px solid Violet;
}
</style>
</head>
<body>
<h3 style="color:blue">로그인</h3>
<form action="Login" method="post">
<table style="border:2px solid Tomato;">
<tr>
<th>ID</th><td><input type="text" name="id"></td>
</tr>
<tr>
<th class="c1">PWD</th><td class="c1"><input type="password" name="pwd"></td>
</tr>
<tr>
<td colspan="2"><input id="test" type="submit" value="login">
<a href="form.jsp">회원가입</a></td>
</tr>
</table>
<br>

</form>
</body>
</html>