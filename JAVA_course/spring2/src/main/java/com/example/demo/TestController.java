package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class TestController { //컨트롤러의 주 역할: 외부에 노출할 url을 정의하고 이 url로 요청이 왔을 때 실행할 코드(함수) 정의
	
	//@RequestMapping: url과 함수 등록. 전송방식 따지지 않음(get이건 post건 따지지 않고 실행시킴)
//	@RequestMapping("/index")
//	public String index() {
//		return "index"; // 뷰페이지 경로 반환 (application.properties에서 앞뒤 경로를 지정해 주었기 때문에 jsp이름만 적어주면 해당 파일을 리턴해줌)
//	}
	
	@RequestMapping("/index")
	public void index() { // 더 간단히하려면 void를 쓰면 된다. (url이름과 같은 jsp파일 실행)
		
	}
	
	/*
	아래 방식은 in,output url이 달라서 url이 많이 등장함
	@RequestMapping("/board/writeForm")
	public String writeForm() {
		return "board/write";
	}
	
	@RequestMapping("/board/write")
	public String write(@ModelAttribute("mv") MsgVo mv) { //커맨드 객체는 자동으로 뷰페이지에 전달 -> 우선 default 생성자로 Vo객체생성하고 해당 form의 name으로 각 setter를 불러 값을 적용시켜준다.		
		return "index";
	}
	*/
	
	// 회원가입 로그인 글쓰기 -> 이런애들은 폼을 보여주고 입력내용을 저장 하는 2단계로 이루어졌기때문에 get, post로 나눠서 같은 url을 사용하면 좋음
	// 글 목록 보기 -> 그냥 @RequestMapping으로 보여주기만 하면 됨
	// 컨트롤러에서 get/post를 구분하는 이유는 회원가입 로그인 글쓰기 작업에서 폼을 원하는지, 입력내용 저장을 원하는지 구분하는 용도
	
	@GetMapping("/board/write")
	public void get_write() {
	
	}
	
	@PostMapping("/board/write")
	public String post_write(@ModelAttribute("mv") MsgVo mv) { //커맨드 객체는 자동으로 뷰페이지에 전달 -> 우선 default 생성자로 Vo객체생성하고 해당 form의 name으로 각 setter를 불러 값을 적용시켜준다.		
		return "index";  // redirect:/ -> 클라이언트가 이 url을 요청한것처럼 만들어서 url을 write로 유지되던것이 index로 맞게 해준다.
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
