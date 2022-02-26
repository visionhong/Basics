package com.example.demo.board;

import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.PrePersist;

import com.example.demo.mem.Member2;

@Entity
public class Board2 {
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY) // auto_increment
	private int num;
	@ManyToOne
	@JoinColumn(name="writer", nullable=false)
	private Member2 writer; // 연관된 테이블 명
	private Date w_date; // sql Date -> util Date
	private String title;
	private String Content;
	
	
	@PrePersist //먼저실행
	public void beforeCreate() {
		w_date = new Date();
	}
	
	// 1:1 관계 => @OneToOne
	// 1:다 관계 => @OneToMany
	// 다:1 관계 => @ManyToOne
	// 다:다 관계 => @ManyToMany
	
	public Board2() {
		
	}
	
	public Board2(int num, Member2 writer, Date w_date, String title, String content) {
		super();
		this.num = num;
		this.writer = writer;
		this.w_date = w_date;
		this.title = title;
		Content = content;
	}

	public int getNum() {
		return num;
	}

	public void setNum(int num) {
		this.num = num;
	}

	public Member2 getWriter() {
		return writer;
	}

	public void setWriter(Member2 writer) {
		this.writer = writer;
	}

	public Date getW_date() {
		return w_date;
	}

	public void setW_date(Date w_date) {
		this.w_date = w_date;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getContent() {
		return Content;
	}

	public void setContent(String content) {
		Content = content;
	}

	
	@Override
	public String toString() {
		return "Board [num=" + num + ", writer=" + writer + ", w_date=" + w_date + ", title=" + title + ", Content="
				+ Content + "]";
	}	
	
}
