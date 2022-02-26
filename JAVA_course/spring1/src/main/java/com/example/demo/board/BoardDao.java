package com.example.demo.board;

import java.util.ArrayList;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

@Mapper 
public interface BoardDao {
	
	@Insert("insert into board(writer, w_date, title, content) values(#{writer},sysdate(), #{title}, #{content})")
	void insert(Board b);
	
	@Select("select * from board where num=#{num}")
	Board selectByNum(@Param("num") int num);
	
	@Select("select * from board where writer=#{writer}")
	ArrayList<Board> selectByWriter(@Param("writer") String Writer);
	
	@Select("select * from board where title like #{title}")
	ArrayList<Board> selectByTitle(@Param("title") String title);
	
	@Select("select * from board order by num")
	ArrayList<Board> selectAll();
	
	@Update("update board set w_date=sysdate(), title=#{title}, content=#{content} where num=#{num}")
	void update(Board b);
	
	@Delete("delete from board where num=#{num}")
	void delete(@Param("num") int num);
}
