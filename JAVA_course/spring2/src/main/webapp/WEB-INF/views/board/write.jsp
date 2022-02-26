<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h3>작성</h3>
<form action="${pageContext.request.contextPath }/board/write" method="post">

<table border="1">

<tr><th>이메일</th><td><input type="text" name="email"></td></tr>
<tr><th>글 비밀번호</th><td><input type="password" name="pwd"></td></tr>
<tr><th>내용</th><td><textarea rows="10" cols="45" name="msg"></textarea></td></tr>
<tr><td colspan="2"><input type="submit" value="save"></td>

</table>
</form>
</body>
</html>




