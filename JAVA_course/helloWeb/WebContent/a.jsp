<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<!-- ��ũ��Ʈ��:jsp���� �ڹ��ڵ� �ۼ� ���� -->
<%

//��û(request): Ŭ���̾�Ʈ ��û. id, pwd=>���Ķ����. 
// ����:response. 


  String id = request.getParameter("id");//�̸��� id�� �� �Ķ������ ���� ������
  System.out.println(id);
  out.print(id+"<br/>");
%>
</body>
</html>