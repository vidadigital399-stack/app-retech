from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import Base, engine, get_db
from app.models.entities import User, Router, LoadJob
from app.schemas.api import (
    UserCreate, LoginRequest, TokenResponse,
    RouterCreate, RouterOut, LoadJobCreate, LoadJobOut
)
from app.services.security import hash_password, verify_password, create_access_token
from app.api.deps import get_current_user

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Retech Control API", version="1.0.0")

@app.get("/health")
def health():
    return {"ok": True, "version": "1.0.0"}

@app.post("/auth/register")
def register(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Email ya registrado")
    user = User(email=payload.email, hashed_password=hash_password(payload.password))
    db.add(user)
    db.commit()
    return {"message": "usuario creado"}

@app.post("/auth/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return TokenResponse(access_token=create_access_token(user.email))

@app.get("/routers", response_model=list[RouterOut])
def list_routers(_: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Router).all()

@app.post("/routers", response_model=RouterOut)
def create_router(payload: RouterCreate, _: User = Depends(get_current_user), db: Session = Depends(get_db)):
    router = Router(**payload.model_dump())
    db.add(router)
    db.commit()
    db.refresh(router)
    return router

@app.get("/jobs", response_model=list[LoadJobOut])
def list_jobs(_: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(LoadJob).all()

@app.post("/jobs", response_model=LoadJobOut)
def create_job(payload: LoadJobCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if not payload.target.startswith(("http://", "https://")):
        raise HTTPException(status_code=400, detail="target debe iniciar con http/https")
    job = LoadJob(**payload.model_dump(), created_by_id=user.id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job
