

from sqlalchemy import Column, Integer, String, delete, insert, select, update

from models import model_to_list
from models.database import Base, db_session


class Fruit(Base):
    __tablename__ = 'fruit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    price = Column(Integer)

    @classmethod
    def insert(cls, fruit_dict: dict):
        stmt = insert(Fruit).values(fruit_dict)
        res = db_session.execute(stmt)
        db_session.commit()
        assert 1 == res.rowcount
        fruit_dict['id'] = res.inserted_primary_key[0]
        return fruit_dict

    @classmethod
    def delete(cls, id: int):
        stmt = delete(Fruit).where(Fruit.id == id)
        res = db_session.execute(stmt)
        db_session.commit()
        assert 1 == res.rowcount

    @classmethod
    def update(cls, id: int, fruit_dict: dict):
        stmt = update(Fruit).values(fruit_dict).where(Fruit.id == id)
        res = db_session.execute(stmt)
        db_session.commit()
        assert 1 == res.rowcount

    @classmethod
    def get(cls, id: int):
        stmt = select(Fruit).where(Fruit.id == id)
        res = db_session.execute(stmt)
        return model_to_list(res)

    @classmethod
    def get_all(cls, offset, limit: int):
        stmt = select(Fruit).limit(limit).offset(offset)
        res = db_session.execute(stmt)
        return model_to_list(res)
