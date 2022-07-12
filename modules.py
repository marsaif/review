from sqlalchemy import Boolean, Text, create_engine
from sqlalchemy import Column , Integer, Text , create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote  
from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


engine = create_engine('sqlite:///reviews.db', echo = True, connect_args={"check_same_thread": False})
Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    first_name = Column(Text(655365))
    last_name = Column(Text(655365))
    email = Column(Text(655365))
    review_title = Column(Text(655365))
    review = Column(Text(655365))
    service = Column(Text(655365))
    job = Column(Text(655365))
    post_code = Column(Text(655365))
    phone_number = Column(Text(655365))
    published = Column(Boolean(),default=False)
    quality = Column(Text(655365))
    tidiness = Column(Text(655365))
    reliability = Column(Text(655365))
    courtesy = Column(Text(655365))
    business = Column(Text(655365))
    def serialize(self):
        d = Serializer.serialize(self)
        return d

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()