<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h3>����</h3>
<a href="/guestbook/write">���ۼ�</a><br>
<table border="1">
<tr><th>�۹�ȣ</th><th>�ۼ���</th><th>�۳���</th></tr>
<c:forEach var="gb" items="${list }">
<tr>
<td>${gb.num }</td><td>${gb.writer }</td><td>${gb.content }</td>
</tr>
</c:forEach>
</table>
</body>
</html>