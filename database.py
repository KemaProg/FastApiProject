from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# Создаем асинхронный движок, который будет отправлять запрос в базу данных
engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db" # URL
)

# Создаем сессию. Это открытие транзакции для работы с базой данных
new_session = async_sessionmaker(engine, expire_on_commit=False) 

class Model(DeclarativeBase):
    ... 
    
    
class TaskOrm(Model): 
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True) 
    name: Mapped[str] 
    description: Mapped[Optional[str]] 
    
async def create_tables(): 
    async with engine.begin() as conn: 
        await conn.run_sync(Model.metadata.create_all) 
        
        
async def delete_tables(): 
    async with engine.begin() as conn: 
        await conn.run_sync(Model.metadata.drop_all) 