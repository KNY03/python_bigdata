todos = []  # 할 일 목록(데이터) 저장


def add_todo():
    """1. 할 일 추가"""
    # 1) 사용자에게 할 일 입력 받기
    # 2) 빈 문자열이면 안내 출력 후 종료
    # 3) {"text": 할일내용, "done": False} 형태로 todos에 추가
    # 4) 추가 완료 메시지 출력
    pass


def show_todos():
    """2. 할 일 목록 조회"""
    # 1) todos가 비어있으면 '할 일이 없습니다' 출력
    # 2) 번호(1부터), 완료 여부(done), 할 일(text) 출력
    pass


def complete_todo():
    """3. 할 일 완료 처리"""
    # 1) todos가 비어있으면 안내 출력
    # 2) 완료할 번호 입력 받기
    # 3) 숫자인지 확인 (isdigit)
    # 4) 인덱스로 변환: idx = int(num) - 1
    # 5) 범위 체크 (0 <= idx < len(todos))
    # 6) todos[idx]["done"] = True 처리
    # 7) 완료 메시지 출력
    pass


def delete_todo():
    """4. 할 일 삭제"""
    # 1) todos가 비어있으면 안내 출력
    # 2) 삭제할 번호 입력 받기
    # 3) 숫자인지 확인 (isdigit)
    # 4) 인덱스로 변환: idx = int(num) - 1
    # 5) 범위 체크 (0 <= idx < len(todos))
    # 6) removed = todos.pop(idx)
    # 7) 삭제 메시지 출력
    pass


def main():
    # 프로그램 반복 실행(메뉴)
    while True:
        print("1) 추가  2) 목록  3) 완료  4) 삭제  0) 종료")
        menu = int(input("메뉴 선택: "))


        if menu == "1":
            # add_todo() 호출
            pass

        elif menu == "2":
            # show_todos() 호출
            pass

        elif menu == "3":
            # complete_todo() 호출
            pass

        elif menu == "4":
            # delete_todo() 호출
            pass

        elif menu == "0":
            # 종료 메시지 출력 후 break
            print("종료합니다./n")
            break

        else:
            print("메뉴를 다시 선택하세요.")


if __name__ == "__main__":
    main()
