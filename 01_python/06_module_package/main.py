'''
py(파이썬 스크립트)와 ipynb(주피터 노트북) 파일의 차이점

py: 파일 전체를 위에서 아래로 한 번에 실행하며 재현 가능한 결과를 낸다.
-> 서비스 코드, 라이브러리, 자동화 스크립트 등에 적합하다.
ipynb: 셀 단위로 실행하며 실행한 셀의 순서대로 변수/객체 상태가 메모리에 남는다.
->학습, 데이터 분석, 시각화, 결과 공유 등에 적합하다.
'''

# 모듈 import 스타일 비교 함수
def demo_import_styles():
    import mymodule                     #모듈 전체 임포트
    print(mymodule.VERSION)
    print(mymodule.Add(1,2))
    print(mymodule.Mutiple(3,4))

    import mymodule as mm               # 별칭(alias) 사용하여 import
    print(mm.VERSION)
    print(mm.Add(5,6))
    print(mm.Mutiple(7,8))

    from mymodule import Add, VERSION   #필요한 것만 import
    print(VERSION)
    print(Add)
    #print(Mutiple)

    from mymodule import Add as a, Mutiple as m     # 특정 요소에 별칭을 부여하며 import
    print(a(10,20))
    print(m(30,40))

# 네임 스페이스 충돌 테스트
def demo_namespace_collision():
    '''
    네임 스페이스(namespace)란?
    변수, 함수, 클래스 등의 이름이 저장되는 공간이다.
    같은 이름이라도 네임스페이스가 다르면 서로 충돌하지 않는다.
    1) Local namespace : 함수 내부에서 생성되는 이름 공간
    2) Global namespace : 현재 파일(.py)의 전역 이름 공간
    3) Module namespace : import 된 모듈 내부의 이름 공간
    '''
    import math_utils
    import string_utils

    print(math_utils.calculator(5))
    print(string_utils.calculator("hi"))

    # from-import는 현재 파일 네임스페이스로 이름을 가져오므로 출돌이 날 수 있다.
    from math_utils import calculator
    from string_utils import calculator
    #print(calculator(10))  -> 이름 충돌로 이전 calculator를 다음 calculator가 덮어씀
    print(calculator("hello"))

# 표준 라이브러리 맛보기
def demo_stdlib_modeuls():
    '''
    표준라이브러리란?
    파이썬을 설치하면 기본으로 함께 제공되는 공식 모듈/패키지 묶음이다.
    별도의 설치 없이 바로 import 해서 사용할 수 있다.
    '''

    # math : 수학 상수/함수 제공
    import math

    # random : 의사 난수(재현 가능), 시뮬레이션/게임/무작위 추천 등에 사용
    import random

    # json : 파이썬 객체 <-> json 문자열 변환 모듈
    # json 은 api 통신/설정 파일/로그 등에 자주 사용되는 양식이다.
    import json

    # dir() : 모듈 내부에 어떤 함수/속성이 있는지 확인할 수 있다.
    #print(dir(math))
    print(math.sqrt(16))    # 제곱근
    print(math.pi)          # 원주율
    print(math.ceil(5.1))   # 올림
    print(math.floor(5.9))  # 내림

    random.seed(42)         # 같은 시드를 주면 같은 결과가 재현된다. (테스트에 유리)
    print(random.randint(1,10))
    print(random.sample(range(1,46),6))

    payload = {'name' : 'hong', 'score' : 95, 'tag' : ['python', 'stdlib']}
    s = json.dumps(payload, ensure_ascii = False)   # dict -> json 문자열
    print('[json] dumps : ', s)
    print(type(s))

    obj = json.loads(s)     # json 문자열 -> dict
    print('[json] loads : ', obj)
    print(type(obj))

def demo_package_import():
    # 전체 경로 import
    import myprojects.utils.calcuator
    print(myprojects.utils.calcuator.VERSION)
    
    # from-import로 간결하게
    from myprojects.utils import calcuator
    print(calcuator.VERSION)

    # 모듈 내부 요소 직접 import
    from myprojects.utils.calcuator import Add,Mutiple
    print(Add(1,2))
    print(Mutiple(3,4))

'''
1) 파이썬 파일을 직접 실행하면 __name__ 값은 "__main__"으로 설정된다.
지금 실행의 시작점이 이 파일이다 라는 뜻이다.
2) 파이썬 파일을 import 해서 사용하면 "__name__" 값이 "파일명"으로 설정 된다.
=> 파일이 import 되었을 때 실행용 코드가 자동으로 호출되면 안되므로 부여하는 조건
(import 했는데 갑자기 print() 함수가 호출 되거나 네트워크 호출이 발생하면 곤란)
'''
if __name__ == "__main__":
    demo_import_styles()
    print('-' * 60)

    demo_namespace_collision()
    print('-' * 60)

    demo_stdlib_modeuls()
    print('-' * 60)
    
    demo_package_import()