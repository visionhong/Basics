<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
function a(){
	// 패이지 이동
	location.href="${pageContext.request.contextPath }/member/success.jsp";
}

</script>


</head>
<body>

<h3>내정보 보기 / 수정</h3>
<form action="${pageContext.request.contextPath }/member/MyInfo" method="post">  <%-- ${pageContext.request.contextPath } -> 기본경로를 의미--%> 
<table border="1">
<tr>
<th>id</th><td><input type="text" value="${m.id }" name="id" readonly></td>  <!-- readonly 는 수정불가능하게 해줌 -->

</tr>
<tr>
<th>pwd</th><td><input type="text" value="${m.pwd }" name="pwd"></td>
</tr>

<tr>
<th>name</th><td><input type="text" value="${m.name }" readonly></td>
</tr>

<tr>
<th>email</th><td><input type="text" value="${m.email }" readonly></td>
</tr>

<tr>
<td colspan="2">
<input type="submit" value="정보수정">
<input type="button" value="확인" onclick="a()">
</td>
</tr>
</table>
</form>








<!-- <table border="1"> -->

<!-- <tr> -->
<!-- <th>id</th> -->
<!-- <th>pwd</th> -->
<!-- <th>name</th> -->
<!-- <th>email</th> -->
<!-- </tr> -->

<!-- <tr> -->
<%-- <td>${m.id }</td> --%>
<%-- <td>${m.pwd }</td> --%>
<%-- <td>${m.name }</td> --%>
<%-- <td>${m.email }</td> --%>
<!-- </tr> -->

<!-- </table> -->

</body>
</html>