<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
//함수 정의. 전역변수 정의
</script>
</head>
<body>
<table border="1">
<script type="text/javascript">
for(k=0;k<2;k++){
	document.write("<tr>");
	for(i=2;i<10;i++){
		if(k==0){
			document.write("<th>"+i+"단</th>");
		}else{
			document.write("<td>");
			for(j=1;j<10;j++){
				document.write(i+' * '+j+' = '+(i*j)+'<br>');
			}
			document.write("</td>");
		}
	}
	document.write("</tr>");
}
</script>
</table>
</body>
</html>