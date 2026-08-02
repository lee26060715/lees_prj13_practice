from model.music import Music, DefaultMusic

music_play_list = DefaultMusic.create_playlist()


# 음악 등록하기
def plus_music():
    while True:
        title = input("추가할 음악 제목: ")
        genre = input("추가한 음악 장르 분류: ")
        artist = input("추가할 음악 아티스트: ")

        m = Music(title, genre,artist)
        music_play_list.append(m)

        answer = input("음악을 더 등록하시겠습니까? (y/n):")
        if answer != "y":
            print("\n플레이리스트 추가를 종료합니다.")
            break


# 플레이 리스트 보기
def play_music_list():
    if not music_play_list:
        print("등록된 음악이 없습니다.")
        return
    print("\n----- 플레이 리스트 -----")
    print("번호 | 제목")
    for idx, m in enumerate(music_play_list):
        print(f"{idx + 1}   | {m.title}")



# 플레이 리스트 상세보기
def view_detail_play_music_list():
    if not music_play_list:
        print("등록된 음악이 없습니다.")
        return

    try:
        print("--- 플레이 리스트 상세보기 ---")
        music_num = int(input("상세보기할 음악 번호 입력: "))
        m = music_play_list[music_num - 1]
        print(m)

    except (ValueError, IndexError):
        print("올바른 번호를 입력해주세요.")


# 플레이리스트 삭제하기
def delete_play_music_list():
    while True:
        if not music_play_list:
            print("등록된 음악이 없습니다.")
            return

        try:
            print("\n--- 플레이 리스트에서 삭제 ---")
            music_num = int(input("플레이리스트에서 삭제할 음악 번호: "))

            del music_play_list[music_num - 1]
            print("플레이 리스트에서 삭제되었습니다.\n")

            answer = input("음악을 더 삭제하시겠습니까? (y/n): ")

            if answer != "y":
                print("\n플레이리스트 삭제를 종료합니다.")
                break

        except (ValueError, IndexError):
            print("올바른 번호를 입력해주세요.")
