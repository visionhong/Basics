package resources;
// config 파일을 읽어와서 실제로 적용하는 코드
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;

import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class Factory {
	 private static SqlSessionFactory sqlSessionFactory;
	 
	    static {
	        try {
	        	String resource = "resources/config.xml";
	            Reader reader = Resources.getResourceAsReader(resource);
	 
	            if (sqlSessionFactory == null) {
	                sqlSessionFactory = new SqlSessionFactoryBuilder().build(reader);
	                
	                Class[] mapper = {mem.Dao.class, board.Dao.class};
	    			for(Class m : mapper){  // DAO Impl을 여기서 대신함
	    				sqlSessionFactory.getConfiguration().addMapper(m);
	    			}
	            }
	        }
	        catch (FileNotFoundException fileNotFoundException) {
	            fileNotFoundException.printStackTrace();
	        }
	        catch (IOException iOException) {
	            iOException.printStackTrace();
	        }
	    }
	    public static SqlSessionFactory getSqlSessionFactory() {
	        return sqlSessionFactory;
	    }
}
