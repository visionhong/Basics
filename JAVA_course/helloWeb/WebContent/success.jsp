<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%
  String id = request.getParameter("id");
%>

<h3><%= id %>님 로그인 성공</h3>
</body>
</html>