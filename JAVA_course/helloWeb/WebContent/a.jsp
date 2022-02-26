<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<!-- 스크립트릿:jsp에서 자바코드 작성 영역 -->
<%

//요청(request): 클라이언트 요청. id, pwd=>폼파라메터. 
// 응답:response. 


  String id = request.getParameter("id");//이름이 id인 폼 파라메터의 값을 꺼내옴
  System.out.println(id);
  out.print(id+"<br/>");
%>
</body>
</html>