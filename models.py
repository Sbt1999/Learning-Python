from sqlalchemy import Column, Integer, String, Text
from database import Base

# represent table
class Resume(Base):
    # table name
    __tablename__ = "resumes"

    id = Column(Integer, primary_key = True, index = True)
    filename = Column(String)
    filepath = Column(String)
    extracted_text =  Column(Text)
