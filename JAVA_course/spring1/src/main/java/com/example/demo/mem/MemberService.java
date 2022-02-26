package com.example.demo.mem;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MemberService {
	@Autowired  // 의존성 자동주입 (new MemberDao를 하지 않아도 dao에 MemberDao와 같은 객체를 만들어줌)
	private MemberDao dao;
	
	public void addMember(Member m) {
		dao.insert(m);
	};
	public Member getMember(String id) {
		return dao.select(id);
	};
	public void editMember(Member m) {
		dao.update(m);
	};
	public void delMember(String id) {
		dao.delete(id);
	};
	public boolean login(String id, String pwd) {
		boolean flag = false;
		Member m = getMember(id);
		if (m != null && pwd.equals(m.getPwd())) {
			flag = true;
		}
		return flag;
	};
	
}
