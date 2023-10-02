from sqlalchemy import Column, String, Text

from sqlalchemy.orm import relationship
# Импортируем базовый класс для моделей.
from app.core.db import Base
from app.models.reservation import Reservation

class MeetingRoom(Base):
    name = Column(String(100), unique=True, nullable=False)
    # Новый атрибут модели. Значение nullable по умолчанию равно True, 
    # поэтому его можно не указывать.
    description = Column(Text)  
    reservations = relationship(Reservation, cascade='delete') 