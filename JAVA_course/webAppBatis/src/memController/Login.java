package memController;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import mem.Service;
import mem.ServiceImpl;

/**
 * Servlet implementation class Login ������ �� ����� ������ �ڹ�����
 */
@WebServlet("/member/Login")
public class Login extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public Login() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub

		RequestDispatcher ds = request.getRequestDispatcher("/member/login.jsp");
		ds.forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		String result = "/member/login.jsp";
		Service service = new ServiceImpl();
		String id = request.getParameter("id");
		String pwd = request.getParameter("pwd");
		boolean flag = service.login(id, pwd);
		//���� ������� ���� ������. �Ķ�=>true:����Ʈ. ���� ������ ���ٸ� ���� �����Ͽ� ��ȯ.false:�������� ���ƶ�. 
		HttpSession session = request.getSession();
		if (flag) {
			session.setAttribute("id", id);
			result = "/member/success.jsp";
		}

		// ���� ������ ������ �̵�
		RequestDispatcher ds = request.getRequestDispatcher(result);
		ds.forward(request, response);
	}

}
