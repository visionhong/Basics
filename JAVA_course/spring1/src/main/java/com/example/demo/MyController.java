package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/// url 요청 종류별 실행할 코드 등록
@Controller
public class MyController {
	@RequestMapping(value="/")  // /는 url이 root를 의미
	public String home() {
		return "index"; // 뷰 페이지 경로
	}
	
	@RequestMapping(value="/hello", method=RequestMethod.GET) // url과 method 지정
	public void hello_get() { //@RequestMapping 메서드의 반환값이 void이면 url과 동일한 경로의 뷰 페이지 실행
		
	}
	
//	@RequestMapping(value="/hello", method=RequestMethod.POST) // url과 method 지정
//	public ModelAndView hello_post(String id, String name) { //@RequestMapping 메서드의 반환값이 void이면 url과 동일한 경로의 뷰 페이지 실행
//		ModelAndView mav = new ModelAndView("hello_result");
//		mav.addObject("id", id);
//		mav.addObject("name", name);
//		return mav;
//	}
	
	// 위와 같은 코드임 (훨씬 간편)
	@RequestMapping(value="/hello", method=RequestMethod.POST) // url과 method 지정
	public String hello_post(@ModelAttribute("v") Vo v) { //커맨드 객체, 자동으로 뷰페이지에 전달, (소문자 클래스명으로 접근해야함 vo.id, vo.name 아니면 (@ModelAttribute("v")로 원하는걸로 바꿀 수 있음 )
		
		return "command";
	}
	
	@RequestMapping("/test1")
	public void test1(Model m) {
//		Model mm = (Model)new ModelMap();
//		mm.addAttribute("ad","ad");  // 직접 생성자를 만들어 담으면 데이터가 뷰패이지로 넘어가지는 못함
		
		m.addAttribute("val1", "aaa"); // 함수의 파라미터로 제공을 하면 저장한 데이터가 뷰페이지랑 공유하게됨
		m.addAttribute("val2", "BBB");
	}
	
	
}








