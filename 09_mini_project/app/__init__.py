"""
app 패키지 진입점.

왜 있는가?
- main.py에서 app 내부 함수들을 깔끔히 import할 수 있도록 정리한다.
"""

from .services import add_log, get_all_logs, find_by_date, sum_by_topic
from .utils import input_non_empty, input_positive_int