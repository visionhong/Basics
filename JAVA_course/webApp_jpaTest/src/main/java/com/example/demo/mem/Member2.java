package com.example.demo.mem;

import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.OneToMany;

import com.example.demo.board.Board2;

@Entity
public class Member2 {
	@Id
	private String id;
	private String pwd;
	private String name;
	private String email;
	// Lazy : 매번 join을 하지 않고 필요할때만 한다.
	@OneToMany(fetch=FetchType.LAZY, mappedBy="writer", cascade=CascadeType.REMOVE)
	private List<Board2> list;
	
	public Member2() {
	}

	public Member2(String id, String pwd, String name, String email) {
		this.id = id;
		this.pwd = pwd;
		this.name = name;
		this.email = email;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPwd() {
		return pwd;
	}

	public void setPwd(String pwd) {
		this.pwd = pwd;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	
	public List<Board2> getList() {
		return list;
	}

	public void setList(List<Board2> list) {
		this.list = list;
	}

	@Override
	public String toString() {
		return "Member [id=" + id + ", pwd=" + pwd + ", name=" + name + ", email=" + email + "]";
	}

}
