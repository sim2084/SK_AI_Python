'''
구조화 데이터 파일
- csv : 표(스프레드 시트) 형태 데이터
- Json : api/설정 파일/로그 등 자주 쓰는 데이터 교환 포멧
'''

from paths import DATA_DIR
import csv
import json

def demo_csv_write_read_sum():
    '''
    csv 파일 기본 흐름
    1) writer로 csv 생성
    2) dictreader로 읽기
    3) amount 합계 계산
    '''

    ledger_csv = DATA_DIR/"ledger_sample.csv"
    rows = [
        ("2025-01-03", "식비", "김밥", "card", 3500, "점심"),
        ("2025-01-04", "교통", "버스", "card", 1500, "출근"),
        ("2025-01-05", "통신", "휴대폰", "acct", 30000, "12월")
    ]

    with open(ledger_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "item", "method", "amount", "note"])
        writer.writerows(rows)

    # 읽기 사용한 금액 합계 구하기
    total = 0
    with open(ledger_csv, "r", encoding="utf-8", newline="") as f:
        dr = csv.DictReader(f)
        for row in dr:
            print(row)
            total += int(row['amount'])      # Dictreader 값은 문자열이므로 int 변환 필요

    print((f'file : {ledger_csv.name}, total : {total}'))

def demo_json_dump_load():
    '''
    json 기본 흐름
    - json.dump(obj, f) : 파이썬 객체 -> 파일
    - json.load(f) : 파일 -> 파이썬 객체
    '''

    profile = {"name":"hong","score":95,"tag":["python","io"]}
    profile_json = DATA_DIR/"profile.json"

    with open(profile_json, "w", encoding = "utf-8") as f:
        json.dump(profile, f, ensure_ascii = False, indent = 2)

    with open(profile_json, "r", encoding = "utf-8") as f:
        loaded = json.load(f)

    print('loaded : ', loaded)