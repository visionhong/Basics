<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
function a(){
	val = f.t1.value;
	f.t2.value= val;
	
}
</script>

</head>
<body>

	<form action="a.jsp" method="post" name="f">
	<input type="text" name="t1" value=""><br>
	<input type="text" name="t2"><br>
	<input type="button" value="copy" onclick="a()">
	
	</form>

</body>
</html>