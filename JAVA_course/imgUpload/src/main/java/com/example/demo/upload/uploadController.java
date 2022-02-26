package com.example.demo.upload;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

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
public class uploadController {
	
	private String path = "c:\\img\\";
	
	@GetMapping("/upload/upload")
	public void uploadForm() {
		
	}
	
	@PostMapping("/upload/upload")
	public String upload(ImgVo iv) {
		MultipartFile f = iv.getFile();
		String fname = f.getOriginalFilename();
		System.out.println(f);
		File ff = new File(path + fname);
		
		try {
			f.transferTo(ff); // 업로드 파일 복사
		} catch(IllegalStateException e) {
			e.printStackTrace();
		} catch(IOException e) {
			e.printStackTrace();
		}
		return "redirect:/upload/list";
	}
	
	@RequestMapping("/upload/list")
	public void list(Model m) {
		File imgDir = new File(path);
		String[] files = imgDir.list();
		m.addAttribute("imgs", files);		
	}
	
	@RequestMapping("/upload/read_img")
	public ResponseEntity<byte[]> read_img(String fname) {
		File f = new File(path+fname); //타겟 파일
		HttpHeaders header = new HttpHeaders();
		ResponseEntity<byte[]> result = null;
		try {
			header.add("Content-Type", Files.probeContentType(f.toPath())); //마임타입(경로에 있는 확장자로 이미지 비디오 텍스트 등을 구분)
			result = new ResponseEntity<byte[]>(FileCopyUtils.copyToByteArray(f), header, HttpStatus.OK);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return result;
		
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}

