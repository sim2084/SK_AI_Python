"""
storage.py
- 이 파일은 "파일 저장/로드" 같은 영속화(persistence) 책임을 가진다.
- 즉, '어디에 어떻게 저장할지'만 다룬다.

왜 분리하는가?
- 서비스 로직은 "무엇을" 해야 하는지에 집중하고,
  저장소(storage)는 "어떻게" 저장/불러올지만 책임지게 해서 유지보수가 쉬워진다.
"""

from pathlib import Path
from .models import StudyLog

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FILE_PATH = DATA_DIR / "logs.txt"

def ensure_data_dir():
    # TODO: data/ 폴더가 없으면 생성한다. (exist_ok=True)
    DATA_DIR.mkdir(exist_ok=True)

def save_log(log: StudyLog):
    # TODO: ensure_data_dir() 호출
    # TODO: FILE_PATH를 "a" 모드로 열고, log.to_line() + "\n"을 append 저장
    ensure_data_dir()
    with open(FILE_PATH, "a", encoding="utf-8") as file:
        file.write(log.to_line() + "\n")

def load_logs():
    # TODO: ensure_data_dir() 호출
    # TODO: FILE_PATH를 "r"로 열고 한 줄씩 읽어 StudyLog 리스트로 반환
    # TODO: 빈 줄은 무시
    # TODO: FileNotFoundError면 빈 리스트 반환
    ensure_data_dir()
    logs = []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == "": 
                    continue
                logs.append(StudyLog.from_line(line))
    except FileNotFoundError:
        return []
    
    return logs