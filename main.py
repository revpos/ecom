from fastapi import FastAPI, Depends

from app.user import UserCreate, UserRead, get_user_service

app = FastAPI(title="rev-store")


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate, service=Depends(get_user_service)):
    new_user = service.create_user(email=user.email, password=user.password)
    return new_user


@app.get("/users", response_model=list[UserRead])
def get_users(service=Depends(get_user_service)):
    return service.get_users()
