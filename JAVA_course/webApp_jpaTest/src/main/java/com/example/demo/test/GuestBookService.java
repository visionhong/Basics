package com.example.demo.test;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class GuestBookService {
	@Autowired
	private GuestBookRepository repos; //dao 생성자라고 생각
	
	
	public void write(GuestBook gb) {
		repos.save(gb); // insert 수행(기본키 값 없음)
	}
	
	public GuestBook getByNum(int num) {
		return repos.getOne(num); // id(primary key)로 한개 검색. select(기본키 기준)	
	}
	
	public ArrayList<GuestBook> getAll(){
		return (ArrayList<GuestBook>) repos.findAll(); // selectAll
	}
	
	public void editBook(GuestBook gb) {
		repos.save(gb);  // id가 없으면 추가이고 있다면 수정을 해줌 // Update(기본키 값 있음)
	}
	public void delBook(int num) {
		repos.deleteById(num); // id(기본키)로 삭제
	}



}
