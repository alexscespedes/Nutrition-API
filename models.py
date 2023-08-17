from database import Base
from sqlalchemy import String, Integer, Column


class Food(Base):
    __tablename__ = 'foods'
    id=Column(Integer, primary_key=True)
    name=Column(String(50), nullable=False, unique=True)
    description=Column(String(75), nullable=False, unique=True)
    type_food=Column(String(25), nullable=False, unique=True)


    def __repr__(self):
        return f"<Food name={self.name} type of food={self.type_food}>"

