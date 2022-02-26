package imgBoard;

public class ImgBoard {
	private int num;
	private String writer;
	private String title;
	private String content;
	private String path;

	public ImgBoard() {
	}

	public ImgBoard(int num, String writer, String title, String content, String path) {
		this.num = num;
		this.writer = writer;
		this.title = title;
		this.content = content;
		this.path = path;
	}

	public int getNum() {
		return num;
	}

	public void setNum(int num) {
		this.num = num;
	}

	public String getWriter() {
		return writer;
	}

	public void setWriter(String writer) {
		this.writer = writer;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public String getPath() {
		return path;
	}

	public void setPath(String path) {
		this.path = path;
	}

	@Override
	public String toString() {
		return "ImgBoard [num=" + num + ", writer=" + writer + ", title=" + title + ", content=" + content + ", path="
				+ path + "]";
	}

}
