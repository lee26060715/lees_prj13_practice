from service.service import plus_music, play_music_list, view_detail_play_music_list, delete_play_music_list


def print_menu():
    print("=====음악 플레이 리스트=====")
# 메뉴 보여주기
    print("1.플레이리스트 등록하기")
    print("2.플레이리스트 보기")
    print("3.플레이리스트 상세보기")
    print("4.플레이리스트에서 삭제하기")
    print("\n0.프로그램 종료\n")
    print("=========================")

# 입력받기
def scan_menu_num():
    menu_num = input("플레이리스트 메뉴 번호 : ")
    return menu_num

# 작업하기
def process(menu_num):
    match menu_num:
        case "0":
            return True
        case "1":
            plus_music()
        case "2":
            play_music_list()
        case "3":
            view_detail_play_music_list()
        case "4":
            delete_play_music_list()
        case _:
            print("잘못 입력하셨습니다.")