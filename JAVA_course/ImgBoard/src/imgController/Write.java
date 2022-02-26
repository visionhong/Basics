package imgController;

import java.io.File;
import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.oreilly.servlet.MultipartRequest;
import com.oreilly.servlet.multipart.DefaultFileRenamePolicy;

import imgBoard.ImgBoard;
import imgBoard.Service;
import imgBoard.ServiceImpl;

/**
 * Servlet implementation class Write
 */
@WebServlet("/img/Write")
public class Write extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public Write() {
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
		RequestDispatcher ds = request.getRequestDispatcher("/imgboard/writeForm.jsp");
		ds.forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setCharacterEncoding("euc-kr");
		request.setCharacterEncoding("euc-kr");
		response.setContentType("text/html; charset=EUC-KR");

		int maxSize = 10 * 1024 * 1024; // ���������� �ִ� ũ��
		String savePath = "C:\\Users\\hong\\eclipse-workspace\\.metadata\\.plugins\\org.eclipse.wst.server.core\\tmp0\\webapps\\img\\";
		String format = "euc-kr";
		String path = "/img/";
		String writer = "";
		String title = "";
		String content = "";
		try {
			// ���� ���ε� ��ü
			MultipartRequest multi = new MultipartRequest(request, savePath, maxSize, format,
					new DefaultFileRenamePolicy());

			writer = multi.getParameter("writer");
			title = multi.getParameter("title");
			content = multi.getParameter("content");
			File f = multi.getFile("file");// ���Ͼ��ε�
			String name = f.getName(); // 경로 뺴고 파일명만 가져옴
			path += name;
		} catch (Exception e) {
			e.printStackTrace();
		}

		ImgBoard ib = new ImgBoard(0, writer, title, content, path);
		Service service = new ServiceImpl();
		service.writeImgboard(ib);
		System.out.println(ib);
		response.sendRedirect(request.getContextPath() + "/img/List");
	}

}
