package com.example.demo;

public class Vo {
	private String id;
	private String name;
	
	public Vo() {}

	public Vo(String id, String name) {
		super();
		this.id = id;
		this.name = name;
	}

	
	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@Override
	public String toString() {
		return "Vo [id=" + id + ", name=" + name + "]";
	}
	
	
	
}
