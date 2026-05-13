from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db.session import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(50), default="admin")

class Router(Base):
    __tablename__ = "routers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    serial: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    model: Mapped[str] = mapped_column(String(120))
    wan_ip: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(30), default="online")

class LoadJob(Base):
    __tablename__ = "load_jobs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    target: Mapped[str] = mapped_column(String(500))
    vus: Mapped[int] = mapped_column(Integer)
    duration_seconds: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(30), default="queued")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    created_by_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_by = relationship("User")
