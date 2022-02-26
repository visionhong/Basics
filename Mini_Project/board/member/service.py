import board.member.dao as mem_dao
import board.member.vo as vo

'''1.가입 2.로그인 3.로그아웃 4.내정보수정 5.탈퇴'''
class Service:
    loginId = None #로그인한 사람의 아이디.
    def __init__(self):
        self.dao = mem_dao.Dao()

    def join(self):
        print('회원가입')
        while True:
            id = input('id:')
            m = self.dao.select(id)
            if m==None:#중복되지 않은 아이디
                break
            else:
                print('중복된 아이디. 다시 입력하시오')

        pwd = input('pwd:')
        name = input('name:')
        email = input('email:')
        self.dao.insert(vo.Member(id, pwd, name, email))

    def login(self):
        id = input('id:')
        m = self.dao.select(id)
        if m==None:
            print('없는 아이디')
        else:
            pwd = input('pwd:')
            if m.pwd==pwd:
                print('로그인 성공')
                Service.loginId = id    #로그인 세션을 유지
            else:
                print('패스워드 불일치')

    def loginCheck(self):
        if Service.loginId==None:
            print('로그인 먼저')
            return False    #로그인 안된 상태
        else:
            return True     #로그인 된 상태

    def logout(self):
        flag = self.loginCheck()
        if flag:
            Service.loginId = None

    def editInfo(self):
        flag = self.loginCheck()
        if flag:
            pwd = input('new pwd:')
            self.dao.update(self.loginId, pwd)

    def out(self):
        flag = self.loginCheck()
        if flag:
            self.dao.delete(self.loginId)
            print('탈퇴완료')
            Service.loginId = None

