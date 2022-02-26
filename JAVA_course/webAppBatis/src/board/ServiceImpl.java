package board;

import java.util.ArrayList;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import board.Dao;
import resources.Factory;

public class ServiceImpl implements Service {
	private SqlSessionFactory sqlSessionFactory;

	public ServiceImpl() {
		sqlSessionFactory = Factory.getSqlSessionFactory();
	}
	
	@Override
	public void writeBoard(Board b) {
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);
		mapper.insert(b);
		session.commit();
		session.close();
	}

	@Override
	public Board getBoard(int num) {
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		Board b = mapper.selectByNum(num);
		session.close();
		return b;
	}

	@Override
	public ArrayList<Board> getByTitle(String title) {
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		ArrayList<Board> list = mapper.selectByTitle(title);
		session.close();
		return list;		
	}

	@Override
	public ArrayList<Board> getByWriter(String writer) {
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		ArrayList<Board> list = mapper.selectByWriter(writer);
		session.close();
		return list;
	}

	@Override
	public ArrayList<Board> getAll() {
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		ArrayList<Board> list = mapper.selectAll();
		session.close();
		return list;
	}

	@Override
	public void editBoard(Board b) {
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		mapper.update(b);
		session.commit();
		session.close();
	}

	@Override
	public void delBoard(int num) {
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		mapper.delete(num);
		session.commit();
		session.close();
	}

}
