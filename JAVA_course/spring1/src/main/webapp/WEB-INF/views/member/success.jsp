<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>

<h3>${sessionScope.id }�� �α��� ����</h3>
<h3><a href="${pageContext.request.contextPath }/member/edit">����������</a></h3>
<h3><a href="${pageContext.request.contextPath }/member/out">Ż��</a></h3>
<h3><a href="${pageContext.request.contextPath }/member/logout">�α׾ƿ�</a></h3>
<h3><a href="${pageContext.request.contextPath }/board/list">�Խ���</a></h3>

</body>
</html>