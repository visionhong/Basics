<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h3>�ۼ� ������</h3>
<form action="${pageContext.request.contextPath }/img/Write" method="post" enctype="multipart/form-data">
<table border="1">
<tr>
<th>�ۼ���</th><td><input type="text" name="writer"></td>
</tr>
<tr>
<th>����</th><td><input type="text" name="title"></td>
</tr>
<tr>
<th>����</th><td><textarea rows="5" cols="45" name="content"></textarea></td>
</tr>
<tr>
<th>��������</th><td><input type="file" name="file"></td>
</tr>
<tr><td colspan="2"><input type="submit" value="�ۼ�"></td></tr>
</table>
</form>
</body>
</html>