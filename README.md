# 📄 Resume Analyzer & Enhancer

This is a Flask-based web application that analyzes uploaded resumes and compares them against a provided job description. It scores the resume based on keyword matching, readability, and essential sections. Additionally, it offers **smart improvement suggestions** to make resumes more impactful.

---

## 🚀 Features

✅ Upload and parse PDF resumes  
✅ Compare against custom job descriptions  
✅ Score based on:
- Keyword relevance
- Readability score
- Section completeness (Education, Experience, Skills, Projects)

✅ Provides actionable suggestions  
✅ (Optional) Rewrites weak resume lines to sound more impactful using AI  
✅ Built with Flask + Bootstrap (frontend)

---

## 🖥️ Demo Screenshot


![Screenshot 2025-07-04 210328](https://github.com/user-attachments/assets/ce08e2dc-6f18-405f-9622-40464dc4e790)
![Screenshot 2025-07-04 210345](https://github.com/user-attachments/assets/cc4337fb-586f-4470-8210-eb1c0ae91f90)


---

## 🔧 Installation
## Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
##  Install Dependencies
pip install -r requirements.txt
## download the SpaCy model
python -m spacy download en_core_web_sm
### 1. Clone the Repository

```bash
https://github.com/Vijaykishore59/resume-score-checker
