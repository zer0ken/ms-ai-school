from .config import *

"""
Note: 
    `.database` 모듈을 먼저 임포트하고 `.models` 모듈을 임포트해야 합니다.
    `.database` 모듈이 완전히 초기화되지 않은 시점에서는
    `.models`에서 db에 새 테이블 모델을 등록할 수 없기 때문입니다.
"""
from .database import db, migrate
from .models import *
