"""
utils.py
- 입력 검증, 출력 포맷 같은 '공통 기능'을 모아둔다.

왜 분리하는가?
- main.py나 services.py가 입력 검증 코드로 지저분해지지 않게 한다.
"""

def input_non_empty(prompt):
    # TODO: 입력값을 strip()한 뒤, 빈 값이면 안내하고 재입력 받는다.
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("빈 값은 입력할 수 없습니다.")

def input_positive_int(prompt):
    # TODO: 정수로 변환(int) 시도 -> ValueError 처리
    # TODO: 0 이하이면 "학습 시간은 1분 이상이어야 합니다." 출력 후 재입력
    # TODO: 정상 입력이면 정수를 반환
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                print("학습 시간은 1분 이상이여야 합니다.")
                continue
            return n
        except ValueError:
            print("정수만 입력하세요.")