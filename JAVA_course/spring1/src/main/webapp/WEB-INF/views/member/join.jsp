<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script src="http://code.jquery.com/jquery-latest.min.js"></script>   
<script>

	$(document).ready(function() { // 이 jsp가 실행되면 먼저 실행되는 함수
		$("#idCheck").click(function() {  // idCheck 버튼이 눌리면 실행
			//ajax요청. 
			$.post( "/member/idCheck", { id: $("#id").val()} ) // post방식으로 요청 + 입력한 아이디값 같이 보냄
		    .done(function( data ) {//ajax요청의 결과를 받아오면 자동으로 실행
		    	$("#idRes").text(data);  // div에 텍스트로 사용가능 or  사용 불가능 출력
		  });
		});
		
		$("#join").click(function() {
			if($("#id").val()==''){
				alert('id는 필수');
				return;
			}
			if($("#pwd").val()==''){
				alert('pwd는 필수');
				return;
			}
			if($("#name").val()==''){
				alert('name는 필수');
				return;
			}
			if($("#email").val()==''){
				alert('email는 필수');
				return;
			}
			
			if($("#idRes").text().trim()!="사용가능"){
				alert('id 중복체크 하시오');
				return;
			}
			$("form").submit();
		});
	});


</script>
</head>
<body>
<h3>회원가입</h3>
<form action="${pageContext.request.contextPath }/member/join" method="post" name='f'>
<input type="hidden" name="flag" value="false">
<table style="border:2px solid black">
<tr>
<th>id</th><td><input type="text" name="id" id="id">
<input type="button" value="id중복체크" id="idCheck">
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
<input type="button" value="가입" id="join">
<input type="reset" value="취소">
</td>
</tr>
</table>
</form>
</body>
</html>