from fastapi import FastAPI, UploadFile, File, Form
from typing import List
import PyPDF2
from sentence_transformers import SentenceTransformer, util
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = SentenceTransformer('all-MiniLM-L6-v2')


def extract_text(file):

    reader = PyPDF2.PdfReader(file.file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


@app.post("/rank")

async def rank_resumes(
    job_description: str = Form(...),
    resumes: List[UploadFile] = File(...)
):

    job_embedding = model.encode(job_description)

    results = []

    for resume in resumes:

        text = extract_text(resume)

        resume_embedding = model.encode(text)

        score = util.cos_sim(job_embedding, resume_embedding)

        results.append({
            "name": resume.filename,
            "score": float(score)
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results
