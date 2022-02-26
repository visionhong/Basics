package com.example.demo.down;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.web.ServerProperties.Tomcat.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.FileCopyUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.multipart.MultipartFile;

@Controller
public class DownFileController {
	@Autowired
	private DownFileService service;
	
	private String basePath = "c:\\down\\";
	
	@GetMapping("/down/upload")
	public void downForm() {
		
	}
	
	@PostMapping("down/upload")
	public String upload(DownFile df) {
			
		MultipartFile ff = df.getFile();
		if(ff==null) {
			System.out.println("file not found");
		}else {
		String fname = ff.getOriginalFilename();
		File f = new File(basePath + fname);
		try {
			ff.transferTo(f);
		} catch (IllegalStateException | IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		df.setPath(fname);
		service.upload(df);
		}
		return "redirect:/down/list";
	}
	
	@RequestMapping("/down/list")
	public void list(Model m) {
		ArrayList<DownFile> list = service.getAll();
		m.addAttribute("list", list);		
		
	}
	
	@RequestMapping("/down/read")
	public void read(Model m, int num) {
		DownFile df = service.getFile(num);
		m.addAttribute("df", df);
	}
	
	@RequestMapping("/down/down")
	public ResponseEntity<byte[]> down(Model m, int num) {
		DownFile df = service.getFile(num);		
		File f = new File(basePath+df.getPath()); //타겟 파일
		HttpHeaders header = new HttpHeaders();
		ResponseEntity<byte[]> result = null;
		try {
			header.add("Content-Type", Files.probeContentType(f.toPath())); //마임타입(경로에 있는 확장자로 이미지 비디오 텍스트 등을 구분)
			header.add(HttpHeaders.CONTENT_DISPOSITION, "attachment;filename=\""+df.getPath()+"\"");  // 다운로드창
			result = new ResponseEntity<byte[]>(FileCopyUtils.copyToByteArray(f), header, HttpStatus.OK);
			service.cntUpdate(num);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return result;
	}
	
	@RequestMapping("/down/del")
	public String del(int num) {
		DownFile df = service.getFile(num);
		service.delFile(num);
		File f = new File(basePath + df.getPath());
		f.delete();
		return "redirect:/down/list";
	}
	
}
