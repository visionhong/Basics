package com.example.demo.board;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
public class BoardController {
	@Autowired
	private BoardService service;
	

	@RequestMapping("/board/list")
	public void list(Model m) {
		ArrayList<Board> list = service.getAll();
		m.addAttribute("list", list);	
	}
	
	@GetMapping("/board/write")
	public void get_writer() {	
	}
	
	@PostMapping("/board/write")
	public String post_writer(Board b) {
		service.writeBoard(b);
		return "redirect:/board/list";
	}
	
	@RequestMapping("/board/read")
	public void read(Model m, int num, String title) {
		Board b = service.getBoard(num);
		m.addAttribute("b", b);
	}
	
	@RequestMapping("/board/search")
	public String search(Model m, String writer, String title, int type) throws UnsupportedEncodingException {
		
		ArrayList<Board> list = null;
		if(type == 1) {
			list = service.getByWriter(writer);
		}else if(type == 2) {
			title = "%" + title + "%";
			list = service.getByTitle(title);	
		}	
		m.addAttribute("list", list);
		return "board/list";
	}
		
	@RequestMapping("/board/edit")
	public String edit(Board b) {
		service.editBoard(b);
		return "redirect:/board/list";
	}
	
	@RequestMapping("/board/del")
	public String del(int num) {
		service.delBoard(num);
		return "redirect:/board/list";
	}
	
}

