"""
Study Log Tracker

이 프로그램은 간단한 CLI 기반 학습 기록 관리 프로그램이다.
사용자가 날짜, 학습 주제, 학습 시간, 메모를 입력하면 파일에 저장하고,
저장된 기록을 조회하거나 주제별 학습 시간을 집계할 수 있다.

main.py
- 메뉴 출력과 흐름 제어(UI)만 담당한다.
- 실제 기능(추가/검색/집계)은 services.py로 위임한다.

왜 이렇게 하는가?
- UI 로직과 비즈니스 로직을 분리하면 코드가 덜 복잡해지고 유지보수가 쉬워진다.
"""

from app import add_log, get_all_logs, find_by_date, sum_by_topic
from app import input_non_empty, input_positive_int

def show_menu():
    print()
    print("1. 기록 추가")
    print("2. 전체 기록 보기")
    print("3. 날짜로 검색")
    print("4. 주제별 학습 시간 합계")
    print("5. 종료")

def run():
    while True:
        show_menu()
        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            date = input_non_empty("날짜(YYYY-MM-DD): ")
            topic = input_non_empty("주제: ")
            minutes = input_positive_int("학습 시간(분): ")
            memo = input_non_empty("메모: ")

            add_log(date, topic, minutes, memo)
            print("저장 완료")

        elif choice == "2":
            logs = get_all_logs()
            if not logs:
                print("저장된 기록이 없습니다.")
            else:
                for log in logs:
                    print(log)

        elif choice == "3":
            target_date = input_non_empty("검색할 날짜(YYYY-MM-DD): ")
            logs = find_by_date(target_date)
            if not logs:
                print("해당 날짜의 기록이 없습니다.")
            else:
                for log in logs:
                    print(log)

        elif choice == "4":
            totals = sum_by_topic()
            if not totals:
                print("저장된 기록이 없습니다.")
            else:
                for topic, total in totals.items():
                    print(f"{topic} : {total}분")

        elif choice == "5":
            print("프로그램을 종료합니다.")
            break

        else:
            print("메뉴를 다시 선택하세요.")

if __name__ == "__main__":
    run()