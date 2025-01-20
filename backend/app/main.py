from fastapi import FastAPI, UploadFile, Form, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud, models
from app.schemas import UserCreate, UserLogin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to restrict origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/auth/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = crud.create_user(db, user.username, user.email, user.password)
    return {"message": "User created successfully", "user": user.username}

@app.post("/api/auth/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, data.email)
    if not user or not crud.verify_password(user.hashed_password, data.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful", "user": {"id": user.id, "name": user.username, "email": user.email}}

# Upload study material
@app.post("/upload/")
async def upload_file(file: UploadFile):
    content = await file.read()
    with open(f"uploaded_files/{file.filename}", "wb") as f:
        f.write(content)
    return {"message": f"Uploaded {file.filename}"}

# Generate a quiz
@app.post("/generate-quiz/")
async def generate_quiz(topic: str = Form(...)):
    # Placeholder logic for quiz generation
    return {"message": f"Generated quiz for topic: {topic}"}

# Handle user queries
@app.get("/query/")
async def query_model(question: str):
    # Placeholder logic for LLM response
    return {"answer": f"Answer to: {question}"}
