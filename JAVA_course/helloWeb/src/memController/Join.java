package memController;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import mem.Member;
import mem.Service;
import mem.ServiceImpl;

/**
 * Servlet implementation class Join
 */
@WebServlet("/member/Join")
public class Join extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Join() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		RequestDispatcher ds = request.getRequestDispatcher("/member/join.jsp");
		ds.forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//한글깨짐 방지
		request.setCharacterEncoding("euc-kr");
		response.setCharacterEncoding("euc-kr");
		response.setContentType("text/html; charset=EUC-KR");
		
		//폼파라메터 load
		String id = request.getParameter("id");
		String pwd = request.getParameter("pwd");
		String name = request.getParameter("name");
		String email = request.getParameter("email");
		
		Service service = new ServiceImpl();
		Member m = new Member(id, pwd, name, email);
		
		service.addMember(m);//회원가입 완료
		
		response.sendRedirect(request.getContextPath()+"/member/login.jsp");  
		// 어떤 작업을 했을때 forward를 쓰고 새로고침을 하면 이 작업이 반복되기 때문에 그런 상황에서는 sendredirect를 써야함.
		//forward를쓰면 login 페이지에 와도 주소창을 보면 아직 join에 있는것을 알 수 있음.
	}

}






