package com.example.demo.mem;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class MemberController {
	@Autowired
	private MemberService service;

	@GetMapping("/member/login")
	public void login_get() {
		
	}
	
	@PostMapping("/member/login")
	public String login_post(String id, String pwd, HttpServletRequest req) {  // 폼양식의 값을 가져옴,일반클래스로 controller를 만들었기 때문에 req는 request객체를 사용하기위함
		// 로그인한 사람의 세션을 받기 위한 req
		String result="member/";
		boolean flag = service.login(id, pwd);
		if(flag) {
			HttpSession session = req.getSession();
			session.setAttribute("id", id);
			result += "success";
		}else {
			result += "login";
		}
		return result;
	}
	
	@GetMapping("/member/join")
	public void join_get() {
		
	}
	
	@PostMapping("/member/join")
	public String join_post(Member2 m) {
		service.addMember(m);
		return "redirect:/member/login";
	}
	
	@RequestMapping("member/idCheck")
	@ResponseBody // 응답을 직접 만들어서 반환
	public String idCheck(String id) {
		String res = "사용불가능";
		Member2 m = service.getMember(id);
		if(m==null) {
			res = "사용가능";
		}
		return res;
	}
	
	@GetMapping("/member/edit")
	public void edit_get(Model model, HttpServletRequest req) {
		HttpSession session = req.getSession();
		String id = (String)session.getAttribute("id");
		Member2 m = service.getMember(id);
		model.addAttribute("m", m);
		
	}
	
	@PostMapping("/member/edit")
	public String edit_post(Member2 m) {
		service.editMember(m);
		return "redirect:/member/success";
	}

	@RequestMapping("/member/success")
	public void success() {
		
	}
		
	@GetMapping("/member/logout")
	public String logout_get(HttpServletRequest req) {
		HttpSession session = req.getSession(false);
		session.invalidate();
		return "redirect:/member/login";
	}
	
	
	@GetMapping("/member/out")
	public String out(HttpServletRequest req) {
		HttpSession session = req.getSession(false);
		String id = (String) session.getAttribute("id");
		service.delMember(id);
		session.invalidate();
		return "redirect:/member/login";	

	}
	
	@PostMapping("/board/getByWriter") // board의 list에서 부름
	public String getByWriter(String writer, Model mm) {
		Member2 m = service.getMember(writer);
		if(m!=null) {
			mm.addAttribute("list", m.getList());
		}	
		return "board/list";	

	}

	
	
	
	
	
	
	
	
	
	

		

}
