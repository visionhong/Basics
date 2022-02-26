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
<% //스크립트릿
	System.out.println("start");
    request.setCharacterEncoding("UTF-8");//인코딩 설정
    int maxSize = 10*1024*1024; //전송파일의 최대 크기
    String savePath = "C:\\img\\";
    String format = "UTF-8";
    String uploadFile="";
    String type = "";
    try{
        MultipartRequest multi = new MultipartRequest(request, savePath, maxSize, format, 
        		new DefaultFileRenamePolicy());
        
         String title = multi.getParameter("title");//입력양식
         type = multi.getParameter("type");
         System.out.println("title:"+title);
         System.out.println("type:"+type);
         //uploadFile = multi.getOriginalFileName("file");
        multi.getFile("file");//파일업로드
        System.out.println("type:"+type);
    }catch(Exception e){
        e.printStackTrace();
    }
    response.sendRedirect("result.jsp");//페이지 이동
%>
</body>
</html>