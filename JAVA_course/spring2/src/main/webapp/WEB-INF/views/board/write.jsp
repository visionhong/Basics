<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h3>�ۼ�</h3>
<form action="${pageContext.request.contextPath }/board/write" method="post">

<table border="1">

<tr><th>�̸���</th><td><input type="text" name="email"></td></tr>
<tr><th>�� ��й�ȣ</th><td><input type="password" name="pwd"></td></tr>
<tr><th>����</th><td><textarea rows="10" cols="45" name="msg"></textarea></td></tr>
<tr><td colspan="2"><input type="submit" value="save"></td>

</table>
</form>
</body>
</html>




