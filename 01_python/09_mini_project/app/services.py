"""
services.py
- 비즈니스 로직(기능)을 담당한다.
- storage.py를 이용해 추가/조회/검색/집계를 구현한다.

왜 분리하는가?
- main.py는 메뉴/흐름 제어만 담당하고,
  기능은 services.py로 분리하면 테스트/확장이 쉬워진다.
"""

from .models import StudyLog
from .storage import save_log, load_logs

def add_log(date, topic, minutes, memo):
    # TODO: StudyLog 객체 생성 후 save_log로 저장
    log = StudyLog(date, topic, minutes, memo)
    save_log(log)

def get_all_logs():
    # TODO: load_logs 결과 반환
    return load_logs()

def find_by_date(target_date):
    # TODO: load_logs를 불러와서 date가 target_date인 것만 필터링해 반환
    logs = load_logs()
    return [log for log in logs if log.date == target_date]

def sum_by_topic():
    # TODO: load_logs를 불러와 topic별 minutes 합계를 dict로 만들어 반환
    logs = load_logs()
    result = {}

    for log in logs:
        if log.topic not in result:
            result[log.topic] = 0           # { "OOP" : 0 }
        result[log.topic] += log.minutes    # { "OOP" : 60 } -> { "OOP" : 120 }
 
    return result