from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class RouterCreate(BaseModel):
    serial: str
    model: str
    wan_ip: str

class RouterOut(RouterCreate):
    id: int
    status: str

class LoadJobCreate(BaseModel):
    target: str
    vus: int = Field(ge=1, le=10000)
    duration_seconds: int = Field(ge=5, le=86400)

class LoadJobOut(LoadJobCreate):
    id: int
    status: str
    created_at: datetime
    created_by_id: int
