<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
function down(){
	location.href="/down/down?num=${df.num}";
}
function del(){
	var pwd = prompt("�� ��й�ȣ�� �Է��϶�");
	if(pwd=='${df.pwd}'){
		location.href="/down/del?num=${df.num}";
	}else{
		alert('�� ��й�ȣ�� ��ġ���� ����')
	}
}
</script>
</head>
<body>
<h3>�� ������</h3>
<a href="/down/list">������� ���ư���</a><br>
<table border="1">
<tr>
<th>�۹�ȣ</th><td>${df.num }<input type="button" value="����" onclick="del()"></td>
</tr>
<tr>
<th>����</th><td>${df.title }</td>
</tr>
<tr>
<th>�ø���</th><td>${df.writer }</td>
</tr>
<tr>
<th>���ϸ�</th><td>${df.path }<input type="button" value="�ٿ�ε�" onclick="down()"></td>
</tr>
<tr>
<th>�ٿ��</th><td>${df.cnt }</td>
</tr>
<tr>
<th>����</th><td>${df.content }</td>
</tr>
</table>
</body>
</html>