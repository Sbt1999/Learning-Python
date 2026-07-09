from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///interview.db"

engine = create_engine(DATABASE_URL)

SesssionLocal = sessionmaker(bind=engine)
Base = declarative_base()

