"""
models.py
- 이 파일은 "데이터 모델"을 정의한다.
- StudyLog는 '학습 기록 1개'를 나타내는 객체이다.

왜 분리하는가?
- 데이터 구조를 한 곳에 모아두면,
  저장 방식(storage)이나 서비스 로직(services)이 바뀌어도 모델은 그대로 재사용할 수 있다.
"""

class StudyLog:
    def __init__(self, date, topic, minutes, memo):
        self.date = date
        self.topic = topic
        self.minutes = minutes
        self.memo = memo

    def to_line(self):
        # TODO: "날짜|주제|분|메모" 형식의 1줄 문자열을 반환한다.
        return f"{self.date}|{self.topic}|{self.minutes}|{self.memo}"

    @staticmethod
    def from_line(line):
        # TODO: line을 split("|")해서 StudyLog 객체로 변환해 반환한다.
        # TODO: minutes는 int로 변환한다.
        date, topic, minutes, memo = line.strip().split("|")
        return StudyLog(date, topic, int(minutes), memo)

    def __str__(self):
        # TODO: 화면 출력용 문자열을 반환한다. 예) "2026-03-05 | file io | 45분 | memo..."
        return f"{self.date} | {self.topic} | {self.minutes} | {self.memo}"