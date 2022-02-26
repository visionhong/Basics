'''
2. 게시판(로그인 상태에서만 사용가능)(vo, dao, service)
  =>1. 글쓰기 2.글목록 3.글번호검색 4. 글 제목으로 검색 5.작성자로 글검색 6.글수정 7.글삭제
'''
import board.article.dao as art_dao
import board.article.vo as art_vo

class Service:

    def __init__(self):
        self.dao = art_dao.DAO()

    def write(self,writer):
        print('글쓰기')

        title = input('title: ')
        content = input('content: ')
        self.dao.insert(art_vo.Board(0, writer, '', title, content))

    def getAll(self):
        print('전체 글 보기')
        datas = self.dao.selectAll()
        for i in datas:
            print(i)

    def getWithNum(self):
        print('글번호 검색')
        num = int(input('검색할 글의 번호: '))
        p = self.dao.numSelect(num)
        if p == None:
            print('글이 없습니다.')
        else:
            print(p)

    def getWithTitle(self):
        print('글 제목 검색')
        title = input('검색할 제목: ')
        datas = self.dao.titleSelect(title)
        if not datas:
            print('해당 제목의 글이 없습니다.')
        else:
            for i in datas:
                print(i)

    def getWithWriter(self):
        print('작성자로 글 검색')
        writer = input('작성자: ')
        datas = self.dao.writerSelect(writer)
        if not datas:
            print('해당 작성자의 글이 없습니다.')
        else:
            for i in datas:
                print(i)

    def editBoard(self,writer):
        print('내가 작성한 글')
        mynum =[]
        datas = self.dao.writerSelect(writer)
        if not datas:
            print('해당 작성자의 글이 없습니다.')
        else:
            for i in datas:
                mynum.append(i.num)
                print(i)

        while True:
            num = int(input('수정할 글의 번호를 입력하세요: '))

            if num not in mynum:
                print('잘못된 번호입니다..')
            else:
                title = input('new title:')
                content = input('new content')
                self.dao.update(art_vo.Board(num,'', '', title, content))
                break

    def delBoard(self,writer):
        print('내가 작성한 글')
        mynum =[]
        datas = self.dao.writerSelect(writer)
        if not datas:
            print('해당 작성자의 글이 없습니다.')
        else:
            for i in datas:
                mynum.append(i.num)
                print(i)

        while True:
            num = int(input('삭제할 글의 번호를 입력하세요: '))

            if num not in mynum:
                print('잘못된 번호입니다..')
            else:
                self.dao.delete(num)
                break




