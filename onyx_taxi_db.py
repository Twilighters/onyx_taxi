from sqlalchemy import Column, Integer, String, create_engine, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

# engine - пул соединений к БД
engine = create_engine('sqlite:///onyx_taxi.db')

# declarative_base - фабричная функция, возвращающая базовый класс, от которого произойдет наследование класса с моделью.
Base = declarative_base()


# Класс, описывающий одну из таблиц БД. Такой класс назывется моделью.
class Driver(Base):
    __tablename__ = 'drivers'  # имя таблицы

    # Атрибуты класса описывают колонки таблицы, их типы данных и ограничения
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Идентификатор водителя")
    name = Column(String(25), nullable=False, comment="Имя водителя")
    car = Column(String(25), comment="автомобиль водителя")

    # переопределение выдачи объекта на экран через print
    def __repr__(self):
        return "<Driver(name={0}, car={1})>".format(self.name, self.car)


class Client(Base):
    __tablename__ = 'clients'  # имя таблицы

    # Атрибуты класса описывают колонки таблицы, их типы данных и ограничения
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Идентификатор клиента")
    name = Column(String(25), nullable=False, comment="Имя клиента")
    is_vip = Column(Boolean, default=False, nullable=False, comment="автомобиль водителя")

    # переопределение выдачи объекта на экран через print
    def __repr__(self):
        return "<Client(name={0}, is_vip={1})>".format(self.name, self.is_vip)


class Order(Base):
    __tablename__ = 'orders'  # имя таблицы

    # Атрибуты класса описывают колонки таблицы, их типы данных и ограничения
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Идентификатор заказа")
    address_from = Column(String(50), nullable=False, comment="Адрес: Откуда")
    address_to = Column(String(50), nullable=False, comment="Адрес: Куда")
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False, comment="Идентификатор клиента")
    driver_id = Column(Integer, ForeignKey('drivers.id'), nullable=False, comment="Идентификатор водителя")
    date_created = Column(DateTime(timezone=True), default=func.now(), comment="Дата и время создания заказа")
    status = Column(String(20), nullable=False, default="not_accepted", comment="Статус")
    client = relationship("Client")
    driver = relationship("Driver")

    # переопределение выдачи объекта на экран через print
    def __repr__(self):
        return "<Order(address_from={0}, address_to={1},client_id={2}, driver_id={3},date_created={4}, status={5},)>".format(
            self.address_from,
            self.address_to,
            self.client_id,
            self.driver_id,
            self.date_created,
            self.status,
        )


if __name__ == "__main__":
    # создание таблиц если они не существуют
    Base.metadata.create_all(engine)

    # создание новой сессии, для выполнения действий
    Session = sessionmaker(bind=engine)
    session = Session()

    # коммит всех изменений
    session.commit()
    session.close()
