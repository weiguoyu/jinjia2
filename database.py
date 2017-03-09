# -*- coding: utf-8 -*-

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    func
)

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import db_url

engine = create_engine(db_url, convert_unicode=True, echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()


class Entries(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False, default="")
    text = Column(Text, nullable=False, default="")

    @classmethod
    def add(cls, title=None, text=None):
        article = cls(
            title=title,
            text=text
        )
        session = db_session()
        session.add(article)
        session.commit()
        return article

    @classmethod
    def get(cls, offset=0, limit=0):
        session = db_session()
        query = session.query(cls).offset(offset).limit(limit)
        return query.all()

    @classmethod
    def get_num(cls,):
        session = db_session()
        query = session.query(func.count(cls.id))
        return query.first()[0]


def init_db():
    Base.metadata.create_all(bind=engine)
