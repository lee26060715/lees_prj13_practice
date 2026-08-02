music_play_list = [("1","fly my wing"),{"2", "compass"},{"3", "saikai"}]

print("\n----- 플레이 리스트 -----")
print("번호 | 제목")
for idx, m in enumerate(music_play_list):
    print(f"{idx}. {m}")
