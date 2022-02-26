<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
function search(type){
	var key = "writer";
	var val = "";
	if(type==2){
		key = "title";
		val = f.title.value;
	}else{
		val = f.writer.value;
	}
	var url = "${pageContext.request.contextPath }/board/Search"
	url += "?"+key+"="+val;
	url += "&type="+type;

	location.href = url;
}
</script>
</head>
<body>
<h3>�۸��</h3>
<a href="${pageContext.request.contextPath }/board/Write">���ۼ�</a><br>
<c:if test="${empty list}">
<h3>��ϵ� ���� ����</h3>
</c:if>
<c:if test="${not empty list}">
<table border="1">
<tr>
<th>�۹�ȣ</th><th>����</th><th>�ۼ���</th><th>�ۼ���</th>
</tr>
<c:forEach var="b" items="${list }">
<tr>
<td>${b.num }</td>
<td><a href="${pageContext.request.contextPath }/board/Read?num=${b.num }">${b.title }</a></td>
<td>${b.writer }</td>
<td>${b.w_date }</td>
</tr>
</c:forEach>
</table>
</c:if>
<form action="" method="post" name="f">
�ۼ��ڷ� �˻�: �ۼ����Է�<input type="text" name="writer"><input type="button" value="�˻�" onclick="search(1)"><br>
�������� �˻�: �˻��ܾ��Է�<input type="text" name="title"><input type="button" value="�˻�" onclick="search(2)"><br>
</form>
</body>
</html>

