<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
   <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
function del(){
	location.href = "${pageContext.request.contextPath }/board/Del?num=${b.num}";
}

</script>
</head>
<body>
<c:if test="${sessionScope.id != b.writer}">
<c:set var="str"> readonly </c:set>
</c:if>
<h3>�� �� ������</h3>
<a href="${pageContext.request.contextPath }/board/List">�۸��</a><br>
<form action="${pageContext.request.contextPath }/board/Edit" method="post">
<table border="1">
<tr><th>�۹�ȣ</th><td><input type="text" name="num" value="${b.num }" readonly></td></tr>
<tr><th>����</th><td><input type="text" name="title" value="${b.title }" ${str} }></td></tr>
<tr><th>�ۼ���</th><td><input type="text" value="${b.writer }" readonly></td></tr>
<tr><th>�ۼ���</th><td><input type="text" value="${b.w_date }" readonly></td></tr>
<tr><th>����</th><td><textarea name="content" rows="15" cols="45" ${str}>${b.content }</textarea></tr>


<c:if test="${sessionScope.id == b.writer}">
<tr><td colspan="2"><input type="submit" value="����">
<input type="button" value="����" onclick="del()"></td></tr>

</c:if>

</table>
</form>
</body>
</html>