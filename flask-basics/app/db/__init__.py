from .database import db, migrate

"""
Note: 
    db가 초기화된 뒤에 `app.models` 모듈을 임포트해서 
    db에 ORM 모델을 등록해야 합니다.
"""
from app.models import *
