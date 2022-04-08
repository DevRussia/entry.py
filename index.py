# 보물상자 오브젝트의 파이선 코드

import Entry

pw = "0"
open_the_case = ""
always_open = 0
wrong_pw = 0
uof0 = 0
no_show_debug = "True"

# 만약 open_the_case가 0이 아니라면 서버점검이라면서 상자 안열어줌ㅋㅋ
# 만약 open_the_case가 0이라면 진짜로 열어줌

def when_start():
    while True:
        if (wrong_pw >= 5):
            Entry.print_for_sec("비번 5회 틀려서 당신은 비번을 1분간 칠수 없습니다", 60)
        Entry.hide_variable("pw")
        Entry.hide_variable("open_the_case")
		Entry.hide_variable("always_open")
		Entry.hide_variable("uof0")
		Entry.hide_variable("no_show_debug")
        pw = random.randint(0, 9999)
        if (Entry.answer() == "시진핑"):
            Entry.print_for_sec("당신은 깨어있는 중국인입니다", 2)
            always_open = True
        open_the_case = random.randint(0, 9999999)
        Entry.input("비번 입력 ㄱㄱㄱ")
        Entry.answer_view("hide")
        if always_open:
            pw = Entry.answer()
        if (Entry.answer() == pw):
            if (open_the_case == 0):
                Entry.print_for_sec("어케했누 ㅋㅋㅋ", 2)
                Entry.change_shape("보물상자2")
                break
            else:
                Entry.print_for_sec("서버가 불안정한 관계로 서버 점검 실시했습니다.", 2)
        else:
            Entry.print_for_sec((("ㅉ 내가 그럴줄 알았다 답은 " + pw) + "다 ㅋ"), 10)
            uof0 += 1
