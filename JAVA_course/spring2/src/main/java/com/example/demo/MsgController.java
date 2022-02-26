package com.example.demo;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class MsgController {

	@Autowired
	private MsgService service;
	
	
	@RequestMapping("/msg/list")
	public void list(Model m) { // 커맨드 객체 -> 뷰페이지로 자동으로 넘어감
		ArrayList<MsgVo> list = service.getAll();
		m.addAttribute("list", list);
	}
	
	@GetMapping("/msg/write")
	public void get_write() {
	
	}
	
	@PostMapping("/msg/write")
	public String post_write(MsgVo mv) { 	
		service.addMsg(mv);
		return "redirect:/msg/list";
	}
	
	@RequestMapping("/msg/edit")
	public String edit(MsgVo mv) {
		service.editMsg(mv);
		return "redirect:/msg/list";
	}

	@RequestMapping("/msg/del")
	public String del(int num) {
		service.delMsg(num);
		return "redirect:/msg/list";
	}
	
	
	
	
}
