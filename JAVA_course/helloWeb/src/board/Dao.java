package board;

import java.util.ArrayList;

public interface Dao {
	void insert(Board b); // 현재날짜로 저장(입력x)
	Board selectByNum(int num); // 글 번호로 검색
	ArrayList<Board> selectByWriter(String writer); // 작성자로 검색
	ArrayList<Board> selectByTitle(String title);  // 제목으로 검색 like활용
	ArrayList<Board> selectAll(); // 전체검색
	void update(Board b); // 글 수정, 글 번호로 찾아서 제목과 내용 변경(날짜는 현재날짜로) 
	void delete(int num); // 글 삭제
}
