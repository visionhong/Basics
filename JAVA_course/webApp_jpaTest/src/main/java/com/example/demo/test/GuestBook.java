package com.example.demo.test;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

// 테이블이라고 알려줌
@Entity
public class GuestBook {
	@Id // primary key 지정
	@GeneratedValue(strategy=GenerationType.IDENTITY) // auto_increment
	private int num;
	private String writer;
	private String content;
	private String pwd;
	
	public GuestBook() {}
	public GuestBook(int num, String writer, String content, String pwd) {
		super();
		this.num = num;
		this.writer = writer;
		this.content = content;
		this.pwd = pwd;
	}
	
	public int getNum() {
		return num;
	}
	public void setNum(int num) {
		this.num = num;
	}
	public String getWriter() {
		return writer;
	}
	public void setWriter(String writer) {
		this.writer = writer;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public String getPwd() {
		return pwd;
	}
	public void setPwd(String pwd) {
		this.pwd = pwd;
	}
	
	@Override
	public String toString() {
		return "GuestBook [num=" + num + ", writer=" + writer + ", content=" + content + ", pwd=" + pwd + "]";
	}
	
}
