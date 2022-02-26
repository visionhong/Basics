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

<h3>사진+정보</h3>

<c:if test="${not empty list }">

<c:forEach var="ib" items="${list }">
<table border="1">
<tr>
<th>num</th><th>writer</th><th>title</th><th>content</th>
</tr>
<tr>
<td>${ib.num }</td><td>${ib.writer }</td><td>${ib.title }</td><td>${ib.content }</td>
</tr>
<img src="${ib.path }" style="width:200px;height:200px;">

</table>
</c:forEach>
</c:if>


</body>
</html>






