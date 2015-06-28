import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.ext import declarative

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = orm.scoped_session(orm.sessionmaker(extension=ZopeTransactionExtension()))


@declarative.as_declarative()
class Base(object):
    @declarative.declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)


class User(Base):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.Text(length=100))
    email = sqlalchemy.Column(sqlalchemy.Text(length=254))
