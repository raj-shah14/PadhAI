from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to restrict origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
