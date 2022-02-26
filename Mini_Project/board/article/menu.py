import board.article.service as serv

class ArtMenu:
    def __init__(self,writer):
        self.service = serv.Service()
        self.writer = writer

    def run(self):
        while True:
            m = int(input('1.글쓰기 2.글목록 3.글번호검색 4.글 제목으로 검색 5.작성자로 글검색 6.글수정 7.글삭제 8.뒤로가기'))
            if m==1:
                self.service.write(self.writer)
            elif m==2:
                self.service.getAll()
            elif m==3:
                self.service.getWithNum()
            elif m==4:
                self.service.getWithTitle()
            elif m==5:
                self.service.getWithWriter()
            elif m==6:
                self.service.editBoard(self.writer)
            elif m ==7:
                self.service.delBoard(self.writer)
            elif m ==8:
                break
