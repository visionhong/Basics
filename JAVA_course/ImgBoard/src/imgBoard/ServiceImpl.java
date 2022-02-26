package imgBoard;

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
	public void writeImgboard(ImgBoard ib) {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		mapper.insert(ib);
		session.commit();// db ���� �۾� ����Ϸ�
		session.close();
	}

	@Override
	public ImgBoard getImgboard(int num) {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		ImgBoard ib = mapper.select(num);
		session.close();
		return ib;
	}

	@Override
	public ArrayList<ImgBoard> getAll() {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		ArrayList<ImgBoard> list = mapper.selectAll();
		session.close();
		return list;
	}

	@Override
	public void editImgboard(ImgBoard ib) {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		mapper.update(ib);
		session.commit();// db ���� �۾� ����Ϸ�
		session.close();
	}

	@Override
	public void delImgboard(int num) {
		// TODO Auto-generated method stub
		SqlSession session = sqlSessionFactory.openSession();// session open
		Dao mapper = (Dao) session.getMapper(Dao.class);// session�� ���� ���� ��ü ȹ��
		mapper.delete(num);
		session.commit();// db ���� �۾� ����Ϸ�
		session.close();
	}

}
