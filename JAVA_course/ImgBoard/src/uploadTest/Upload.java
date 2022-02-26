package uploadTest;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.oreilly.servlet.MultipartRequest;
import com.oreilly.servlet.multipart.DefaultFileRenamePolicy;

/**
 * Servlet implementation class Upload
 */
@WebServlet("/Upload")
public class Upload extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Upload() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setCharacterEncoding("euc-kr");
		request.setCharacterEncoding("euc-kr");
		response.setContentType("text/html; charset=EUC-KR");
		
	    int maxSize = 10*1024*1024; //���������� �ִ� ũ��
	    String savePath = "C:\\img\\";
	    String format = "euc-kr";
	    String uploadFile="";
	    
	    try{
	    	//���� ���ε� ��ü
	        MultipartRequest multi = new MultipartRequest(request, savePath, maxSize, format, 
	        		new DefaultFileRenamePolicy());
	        
	         String title = multi.getParameter("title");//�Է¾��
	         
	         System.out.println("title:"+title);
	         
	         //uploadFile = multi.getOriginalFileName("file");
	        multi.getFile("file");//���Ͼ��ε�
	        
	    }catch(Exception e){
	        e.printStackTrace();
	    }
	    
	    response.getWriter().print("<html><body><h3>upload success</h3></body></html>");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
