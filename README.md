# 🤖 AI Resume Screening System

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![NLP](https://img.shields.io/badge/NLP-SentenceTransformers-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Project Overview

The **AI Resume Screening System** is a full‑stack web application designed to help recruiters automatically analyze and rank resumes based on their relevance to a given job description.

The system uses **Natural Language Processing (NLP)** and **semantic similarity techniques** to compare candidate resumes with job requirements and generate a ranked list of candidates.

This project simulates a simplified **Applicant Tracking System (ATS)** used by modern companies to speed up the candidate shortlisting process.

It demonstrates integration of:

* Frontend development (HTML, CSS, JavaScript)
* Backend API development using **FastAPI**
* **NLP embeddings** for resume similarity
* PDF resume parsing
* Client‑server communication

---

# 🖥️ Demo

### Resume Ranking Interface

Add screenshots of your UI here after running the project.

```
Example:

<img width="521" height="424" alt="image" src="https://github.com/user-attachments/assets/53b922fe-0576-4905-8fdf-c7ce28ed7033" />

```

### Example Result

```
Rank 1 : John_Doe.pdf
Score  : 0.87

Rank 2 : Jane_Smith.pdf
Score  : 0.74

Rank 3 : Alex_Kumar.pdf
Score  : 0.62
```

---

# 🚀 Features

### 📄 Resume Upload

Upload one or multiple resumes in **PDF format**.

### 📝 Job Description Input

Enter a job description or required skills for a role.

### 🧠 AI-Based Resume Analysis

Uses **Sentence Transformers** to convert text into semantic embeddings.

### 📊 Automatic Candidate Ranking

Resumes are ranked based on similarity with the job description.

### 📈 Clean Dashboard Interface

Results are displayed in a simple and readable UI.

---

# 🏗️ System Architecture

```
            +-------------------+
            |   Frontend UI     |
            | HTML / CSS / JS   |
            +---------+---------+
                      |
                      |
                      v
            +-------------------+
            |    FastAPI API    |
            |  Backend Server   |
            +---------+---------+
                      |
                      |
                      v
            +-------------------+
            |   NLP Processing  |
            | SentenceTransform |
            +---------+---------+
                      |
                      |
                      v
            +-------------------+
            | Resume Ranking    |
            | Similarity Score  |
            +-------------------+
```

---

# 🧰 Technology Stack

## Frontend

* HTML
* CSS
* JavaScript

## Backend

* FastAPI
* Uvicorn

## AI / NLP

* Sentence Transformers
* Cosine Similarity

## File Processing

* PyPDF2

---

# 📁 Project Structure

```
AI-Resume-Screener
│
├── backend
│   ├── main.py
│   ├── requirements.txt
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots
│   └── app_ui.png
│
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/AI-Resume-Screener.git
cd AI-Resume-Screener
```

---

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 3️⃣ Run the Backend Server

Navigate to the backend folder:

```
cd backend
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

API Documentation (Swagger UI):

```
http://127.0.0.1:8000/docs
```

---

## 4️⃣ Run the Frontend

Open the frontend file in your browser:

```
frontend/index.html
```

Upload resumes and enter a job description to start ranking.

---

# 📊 Example Workflow

1. User enters a **job description**.
2. User uploads multiple **candidate resumes**.
3. Frontend sends data to the **FastAPI backend**.
4. Backend extracts text from the uploaded PDFs.
5. NLP model converts text to **embeddings**.
6. **Cosine similarity** compares resume with job description.
7. Candidates are **ranked by relevance score**.
8. Results are returned and displayed in the UI.

---

# 🌍 Real‑World Applications

This system can be used for:

* Resume shortlisting for recruiters
* Applicant Tracking Systems (ATS)
* HR automation platforms
* AI-powered hiring tools
* Talent analytics systems

---

# 🔮 Future Improvements

Potential enhancements for this project:

* 🔎 Skill extraction from resumes
* 📉 Missing skills detection
* 📊 Visualization dashboards (charts & analytics)
* 🤖 AI feedback for candidates
* ☁️ Cloud deployment
* 📄 Support for DOCX resumes
* 🧾 Resume ATS scoring

---

# 📚 Learning Outcomes

This project demonstrates knowledge of:

* Full‑stack web development
* REST API development
* Natural Language Processing
* Transformer embeddings
* File parsing and processing
* Client‑server architecture

---


