<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h3>���ۼ�</h3>
<a href="${pageContext.request.contextPath }/board/List">�۸��</a><br>
<form action="${pageContext.request.contextPath }/board/Write" method="post">
<table border="1">
<tr><th>�ۼ���</th><td><input type="text" name="writer" value="${sessionScope.id }" readonly></td></tr>
<tr><th>����</th><td><input type="text" name="title"></td></tr>
<tr><th>����</th><td><textarea name="content" rows="15" cols="45"></textarea></tr>
<tr><td colspan="2"><input type="submit" value="����"></td></tr>
</table>
</form>
</body>
</html>