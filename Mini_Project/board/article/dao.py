import pymysql
import board.article.vo as art_vo

class DAO:

    def connect(self):
        return pymysql.connect(host='localhost', user='testuser', password='testpw',
                       db='testdb', charset='utf8')

    def insert(self,m):
        sql = 'insert into board(writer,w_date,title,content) values(%s,now(),%s,%s)'
        d = (m.writer, m.title, m.content)
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql,d)
        conn.commit()
        conn.close()

    def selectAll(self):
        conn = self.connect()
        sql = 'select * from board'
        cursor = conn.cursor()
        cursor.execute(sql)
        datas = []

        for row in cursor:
            datas.append(art_vo.Board(row[0], row[1], row[2], row[3], row[4]))
        conn.close()
        return datas

    def numSelect(self,num):
        conn = self.connect()
        sql = 'select * from board where num = %s'
        cursor = conn.cursor()
        cursor.execute(sql, num)
        row = cursor.fetchone()
        conn.close()
        if row != None:
            return art_vo.Board(row[0], row[1], row[2], row[3], row[4])

    def titleSelect(self,title):
        conn = self.connect()
        sql = 'select * from board where title like \'%' + title + '%\''
        cursor = conn.cursor()
        cursor.execute(sql)
        datas = []
        for row in cursor:
            datas.append(art_vo.Board(row[0], row[1], row[2], row[3], row[4]))
        conn.close()
        return datas

    def writerSelect(self,writer):
        conn = self.connect()
        sql = 'select * from board where writer = %s'
        cursor = conn.cursor()
        cursor.execute(sql, writer)
        datas = []
        for row in cursor:
            datas.append(art_vo.Board(row[0], row[1], row[2], row[3], row[4]))
        conn.close()
        return datas


    def update(self,m): # 아직
        sql = 'update board set w_date = now() , title=%s, content=%s where num=%s'
        conn = self.connect()
        cursor = conn.cursor()
        d = (m.title, m.content, m.num)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()

    def delete(self,num):
        conn = self.connect()
        sql = 'delete from board where num=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, num)
        conn.commit()  # 쓰기 완료
        conn.close()