from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:todos@127.0.0.1:3306/todos"
#echo true: 어떤 sql이 사용되는 시점에 sql을 print해주는 기능
engine = create_engine(DATABASE_URL, echo=True)

#세션 팩토리를 활용하여 세션 인스턴스와 통신
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    session = SessionFactory()
    try:
        yield  session
    finally:
        session.close()