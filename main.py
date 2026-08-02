from menu.view import print_menu, scan_menu_num, process

# 프로그램 종료

while True:
    print_menu()
    x = scan_menu_num()
    is_exit = process(x)
    if is_exit:  break

    input("\n메뉴로 돌아가려면 Enter를 누르세요...\n")