package com.example.demo.mem;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MemberService {
	@Autowired  // 의존성 자동주입 (new MemberDao를 하지 않아도 dao에 MemberDao와 같은 객체를 만들어줌)
	private MemberRepository repos;
	
	public void addMember(Member2 m) {
		repos.save(m);
	};
	public Member2 getMember(String id) {
		return repos.findById(id).orElse(null); // 기본키가 있으면 객체 반환하고 없으면 null값 반환
	};
	public void editMember(Member2 m) {
		repos.save(m);
	};
	public void delMember(String id) {
		repos.deleteById(id);
	};
	public boolean login(String id, String pwd) {
		boolean flag = false;
		Member2 m = getMember(id);
		if (m != null && pwd.equals(m.getPwd())) {
			flag = true;
		}
		return flag;
	};
	
}
