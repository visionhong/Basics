<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@page import="com.oreilly.servlet.MultipartRequest" %>
<%@page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy" %>
<%@page import="java.io.*" %>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<% //��ũ��Ʈ��
	System.out.println("start");
    request.setCharacterEncoding("UTF-8");//���ڵ� ����
    int maxSize = 10*1024*1024; //���������� �ִ� ũ��
    String savePath = "C:\\img\\";
    String format = "UTF-8";
    String uploadFile="";
    String type = "";
    try{
        MultipartRequest multi = new MultipartRequest(request, savePath, maxSize, format, 
        		new DefaultFileRenamePolicy());
        
         String title = multi.getParameter("title");//�Է¾��
         type = multi.getParameter("type");
         System.out.println("title:"+title);
         System.out.println("type:"+type);
         //uploadFile = multi.getOriginalFileName("file");
        multi.getFile("file");//���Ͼ��ε�
        System.out.println("type:"+type);
    }catch(Exception e){
        e.printStackTrace();
    }
    response.sendRedirect("result.jsp");//������ �̵�
%>
</body>
</html>