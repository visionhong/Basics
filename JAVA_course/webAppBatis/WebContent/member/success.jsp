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
<h3><a href="${pageContext.request.contextPath }/member/List">��� ȸ�� ��� ����</a></h3>
<h3><a href="${pageContext.request.contextPath }/member/MyInfo">����������</a></h3>
<h3><a href="${pageContext.request.contextPath }/member/Out">Ż��</a></h3>
<h3><a href="${pageContext.request.contextPath }/member/Logout">�α׾ƿ�</a></h3>
<h3><a href="${pageContext.request.contextPath }/board/List">�Խ���</a></h3>

</body>
</html>