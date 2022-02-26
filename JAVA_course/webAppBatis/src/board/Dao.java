package board;

import java.util.ArrayList;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

public interface Dao {
	
	@Insert("insert into board(writer, w_date, title, content) values(#{writer},sysdate(),#{title},#{content})")
	void insert(Board b); // 현재날짜로 저장(입력x)
	
	@Select("select * from board where num=#{num}")
	Board selectByNum(@Param("num") int num); // 글 번호로 검색
	
	@Select("select * from board where writer=#{writer}")
	ArrayList<Board> selectByWriter(@Param("writer") String writer); // 작성자로 검색
	
	@Select("select * from board where title like #{title}")
	ArrayList<Board> selectByTitle(@Param("title") String title);  // 제목으로 검색 like활용
	
	@Select("select * from board order by num")
	ArrayList<Board> selectAll(); // 전체검색
	
	@Update("update board set w_date=sysdate(), title=#{title}, content=#{content} where num=#{num}")
	void update(Board b); // 글 수정, 글 번호로 찾아서 제목과 내용 변경(날짜는 현재날짜로)
	
	@Delete("delete from board where num=#{num}")
	void delete(int num); // 글 삭제
}


