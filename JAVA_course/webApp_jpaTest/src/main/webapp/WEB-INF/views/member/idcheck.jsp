<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
//window.onload: �������� ���۵ɶ� �̺�Ʈ �ڵ鷯 ��� �Ӽ�
window.onload=function(){//�͸��Լ�
	var html = '';
	if('${flag}'=='true'){
		html = '��밡���� ���̵�';
		html += '<input type=button value="����" onclick=a()>';
	}else if('${flag}'=='false'){
		html = '�ߺ��� ���̵�';
	}else{
		//window.opener: ��â�� �� �����
		id = window.opener.document.f.id.value;
		ff.id.value = id;
	}
	
	if(html!=''){
		var resDiv = document.getElementById('res');
		resDiv.innerHTML = html;
	}
}

function a(){
	window.opener.document.f.id.value = '${id }';
	window.opener.document.f.flag.value = 'true';
	window.close();
}
</script>
</head>
<body>
<h3>id �ߺ�üũ</h3>
<form action="${pageContext.request.contextPath }/member/idCheck" method="post" name="ff">
id:<input type="text" name="id" value="${id }"><input type="submit" value="�ߺ�üũ">
</form><br>
<div id="res"></div>
</body>
</html>