import pymysql
import board.member.vo as mem

class Dao:
    def connect(self):
        return pymysql.connect(host='localhost', user='testuser', password='testpw',
                       db='testdb', charset='utf8')

    def insert(self, m):
        conn = self.connect()
        sql = 'insert into customer values(%s, %s, %s, %s)'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (m.id, m.pwd, m.name, m.email)
        cursor.execute(sql, d)
        conn.commit()  # 쓰기 완료
        conn.close()

    def select(self, id):
        conn = self.connect()
        sql = 'select * from customer where id=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, id)  # sql실행. 실행한 결과는 cursor 객체에 담아
        row = cursor.fetchone()#검색 결과 한줄추출
        conn.close()
        if row != None:
            return mem.Member(row[0], row[1], row[2], row[3])

    def update(self, id, pwd):# 수정할 제품번호와 새 가격을 Test 객체로 받아옴
        conn = self.connect()
        sql = 'update customer set pwd=%s where id=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (pwd, id)
        cursor.execute(sql, d)
        conn.commit()  # 쓰기 완료
        conn.close()

    def delete(self, id):
        conn = self.connect()
        sql = 'delete from customer where id=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, id)
        conn.commit()  # 쓰기 완료
        conn.close()