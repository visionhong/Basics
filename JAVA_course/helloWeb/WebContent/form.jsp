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
	
	var idx = f.grade.options.selectedIndex;//select에서 선택한 option의 인덱스
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
<h3>회원가입</h3>
<!-- 폼양식: 사용자 입력 인터페이스. 서버 전송 -->
<!-- <form action="서버페이지" method=get/post> -->
<!-- get: url? 뒤에 전송 파라메터를 붙여서 보냄. 보안에 취약. 길이에 제약. -->
<!-- post: 전송 패킷 헤더에 담아 보냄. 데이터가 url에 노출 안됨. 길이에 제약 없음 -->
<form action="Join" method="post" name='f'>
id:<input type="text" name="id"><br>
pwd:<input type="password" name="pwd"><br>
name:<input type="text" name="name"><br>
email:<input type="text" name="email"><br>
성별: <input type="radio" name="gen" value="f">여자
<input type="radio" name="gen" value="m">남자<br>
취미: <input type="checkbox" name="hobby" value="1">수영
<input type="checkbox" name="hobby" value="2">낚시
<input type="checkbox" name="hobby" value="3">여행
<input type="checkbox" name="hobby" value="4">축구  <br>
<select name="grade">
<option value="g1">1학년</option>
<option value="g2">2학년</option>
<option value="g3">3학년</option>
<option value="g4">4학년</option>
</select><br>
<textarea name="info" cols=45 rows="10">가입인사 입력</textarea><br>
<input type="button" value="전송">
<input type="reset" value="취소">
<input type="button" value="일반버튼" onclick="a()"><br>
<input type="text" name="ch">
<input type="button" value="div글자변경" onclick="b()">
</form>
<div id="test">
</div>

</body>
</html>