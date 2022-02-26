import board.member.menu as m1
import board.article.menu as m2
import board.member.service as memserv

## 제목검색할때  조금만써도 나오게
def main():
    mem_menu = m1.MemMenu()
    while True:
        m = int(input('1.회원관리 2.게시판 3.종료'))
        if m==1:
            mem_menu.run()
        elif m==2:#로그인 되어있어야 사용 가능하도록 구현
            writer = memserv.Service.loginId
            if writer !=None:
                art_menu = m2.ArtMenu(writer)
                art_menu.run()
            else:
                print('로그인 먼저')
        elif m==3:
            break

main()