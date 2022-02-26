<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h3>로그인</h3>
<form action="/helloWeb/member/Login" method="post">
<table style="border:2px solid Tomato;">
<tr>
<th>ID</th><td><input type="text" name="id"></td>
</tr>
<tr>
<th>PWD</th><td><input type="password" name="pwd"></td>
</tr>
<tr>
<td colspan="2"><input type="submit" value="login"></td>
</tr>
</table>
<br>
<a href="/helloWeb/member/Join">회원가입</a>
</form>
</body>
</html>