<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
function check(){
	if(f.id.value==''){
		alert('id�� �ʼ�');
		return;
	}
	if(f.pwd.value==''){
		alert('pwd�� �ʼ�');
		return;
	}
	if(f.name.value==''){
		alert('name�� �ʼ�');
		return;
	}
	if(f.email.value==''){
		alert('email�� �ʼ�');
		return;
	}
	
	if(f.flag.value!='true'){
		alert('id �ߺ�üũ �ʼ�');
		return;
	}
	
	f.submit();//���۹�ư Ŭ���� ����
}
function idCheck(){
	//��â ���� �Լ�. p1:��â�����ҽ����, p2:��â�̸�. p3:â����(ũ��, ��ġ...)
	win = window.open("${pageContext.request.contextPath }/member/idcheck.jsp","win","width=500,height=300,top=100,left=100");
}
</script>
</head>
<body>
<h3>ȸ������</h3>
<form action="${pageContext.request.contextPath }/member/Join" method="post" name='f'>
<input type="hidden" name="flag" value="false">
<table style="border:2px solid black">
<tr>
<th>id</th><td><input type="text" name="id"><input type="button" value="id�ߺ�üũ" onclick="idCheck()"></td>
</tr>
<tr>
<th>pwd</th><td><input type="password" name="pwd"></td>
</tr>
<tr>
<th>name</th><td><input type="text" name="name"></td>
</tr>
<tr>
<th>email</th><td><input type="text" name="email"></td>
</tr>
<tr>
<td colspan="2">
<input type="button" value="����" onclick="check()">
<input type="reset" value="���">
</td>
</tr>
</table>
</form>
</body>
</html>