<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script src="http://code.jquery.com/jquery-latest.min.js"></script>   
<script>

	$(document).ready(function() { // �� jsp�� ����Ǹ� ���� ����Ǵ� �Լ�
		$("#idCheck").click(function() {  // idCheck ��ư�� ������ ����
			//ajax��û. 
			$.post( "/member/idCheck", { id: $("#id").val()} ) // post������� ��û + �Է��� ���̵� ���� ����
		    .done(function( data ) {//ajax��û�� ����� �޾ƿ��� �ڵ����� ����
		    	$("#idRes").text(data);  // div�� �ؽ�Ʈ�� ��밡�� or  ��� �Ұ��� ���
		  });
		});
		
		$("#join").click(function() {
			if($("#id").val()==''){
				alert('id�� �ʼ�');
				return;
			}
			if($("#pwd").val()==''){
				alert('pwd�� �ʼ�');
				return;
			}
			if($("#name").val()==''){
				alert('name�� �ʼ�');
				return;
			}
			if($("#email").val()==''){
				alert('email�� �ʼ�');
				return;
			}
			
			if($("#idRes").text().trim()!="��밡��"){
				alert('id �ߺ�üũ �Ͻÿ�');
				return;
			}
			$("form").submit();
		});
	});


</script>
</head>
<body>
<h3>ȸ������</h3>
<form action="${pageContext.request.contextPath }/member/join" method="post" name='f'>
<input type="hidden" name="flag" value="false">
<table style="border:2px solid black">
<tr>
<th>id</th><td><input type="text" name="id" id="id">
<input type="button" value="id�ߺ�üũ" id="idCheck">
<div id="idRes"></div>
</td>
</tr>
<tr>
<th>pwd</th><td><input type="password" name="pwd" id="pwd"></td>
</tr>
<tr>
<th>name</th><td><input type="text" name="name" id="name"></td>
</tr>
<tr>
<th>email</th><td><input type="text" name="email" id="email"></td>
</tr>
<tr>
<td colspan="2">
<input type="button" value="����" id="join">
<input type="reset" value="���">
</td>
</tr>
</table>
</form>
</body>
</html>