<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
function a(){
	var id = f.id.value;
	var pwd = f.pwd.value;
	var name = f.name.value;
	var email = f.email.value;
	
	var txt = 'id:'+id+'\n';
	txt += 'pwd:'+pwd+'\n';
	txt += 'name:'+name+'\n';
	txt += 'email:'+email+'\n';
	alert(txt);
	
	for(i=0;i<f.gen.length;i++){
		if(f.gen[i].checked){
			alert(f.gen[i].value);
		}
	}
	txt = '';
	for(i=0;i<f.hobby.length;i++){
		if(f.hobby[i].checked){
				txt+=f.hobby[i].value+' / ';
		}
	}
	alert(txt);
	
	var idx = f.grade.options.selectedIndex;//select���� ������ option�� �ε���
	txt = f.grade.options[idx].value;
	alert('select:'+txt);
	
	alert(f.info.value);
	
	opt = document.getElementsByTagName('option')[idx];
	txt = opt.innerText;
	alert(txt);
	
	myDiv = document.getElementById('test');
	txt = myDiv.innerHTML;
	alert('test:'+txt);
}

function b(){
	var txt = f.ch.value;
	myDiv = document.getElementById('test');
	myDiv.innerHTML = '<h3>'+txt+'</h3>';
}


</script>
</head>
<body>
<h3>ȸ������</h3>
<!-- �����: ����� �Է� �������̽�. ���� ���� -->
<!-- <form action="����������" method=get/post> -->
<!-- get: url? �ڿ� ���� �Ķ���͸� �ٿ��� ����. ���ȿ� ���. ���̿� ����. -->
<!-- post: ���� ��Ŷ ����� ��� ����. �����Ͱ� url�� ���� �ȵ�. ���̿� ���� ���� -->
<form action="Join" method="post" name='f'>
id:<input type="text" name="id"><br>
pwd:<input type="password" name="pwd"><br>
name:<input type="text" name="name"><br>
email:<input type="text" name="email"><br>
����: <input type="radio" name="gen" value="f">����
<input type="radio" name="gen" value="m">����<br>
���: <input type="checkbox" name="hobby" value="1">����
<input type="checkbox" name="hobby" value="2">����
<input type="checkbox" name="hobby" value="3">����
<input type="checkbox" name="hobby" value="4">�౸  <br>
<select name="grade">
<option value="g1">1�г�</option>
<option value="g2">2�г�</option>
<option value="g3">3�г�</option>
<option value="g4">4�г�</option>
</select><br>
<textarea name="info" cols=45 rows="10">�����λ� �Է�</textarea><br>
<input type="button" value="����">
<input type="reset" value="���">
<input type="button" value="�Ϲݹ�ư" onclick="a()"><br>
<input type="text" name="ch">
<input type="button" value="div���ں���" onclick="b()">
</form>
<div id="test">
</div>

</body>
</html>