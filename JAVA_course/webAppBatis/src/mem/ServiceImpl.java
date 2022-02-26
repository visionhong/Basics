package mem;

import java.util.ArrayList;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import resources.Factory;

public class ServiceImpl implements Service {
	private SqlSessionFactory sqlSessionFactory;

	public ServiceImpl() {
		sqlSessionFactory = Factory.getSqlSessionFactory();
	}

	@Override
	public void addMember(Member m) {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		mapper.insert(m);
		session.commit();  // db 쓰기작업 완료하기 위해 commit 사용해야 함
		session.close();
	}

	@Override
	public Member getMember(String id) {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		Member m = mapper.select(id);
		session.close();
		return m;
	}

	@Override
	public ArrayList<Member> getAll() {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		ArrayList<Member> list = mapper.selectAll();
		session.close();
		return list;
	}

	@Override
	public void editMember(Member m) {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		mapper.update(m);
		session.commit();
		session.close();
	}

	@Override
	public void delMember(String id) {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		mapper.delete(id);
		session.commit();
		session.close();
	}

	@Override
	public boolean login(String id, String pwd) {
		// TODO Auto-generated method stub
		boolean flag = false;
		Member m = getMember(id);
		if (m != null && pwd.equals(m.getPwd())) {
			flag = true;
		}
		return flag;
	}

}
