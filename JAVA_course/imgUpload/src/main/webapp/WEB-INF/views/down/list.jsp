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
<h3>�ڷ��</h3>

<a href="/down/upload">�ڷ���</a>
<table border="1">
<tr>
<th>�۹�ȣ</th><th>����</th><th>�ٿ��</th>
</tr>
<c:forEach var="df" items="${list }">
<tr>
<td>${df.num }</td>
<td><a href="/down/read?num=${df.num}">${df.title }</a></td>
<td>${df.cnt }</td>
</tr>
</c:forEach>

</table>



</body>
</html>