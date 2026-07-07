from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLAlchemy_DATABASE_URL = "mysql+pymysql://root:10112007@localhost:3306/db_test"

engine = create_engine(SQLAlchemy_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()