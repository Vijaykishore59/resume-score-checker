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

![screenshot](screenshots/result.png)

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
git clone https://github.com/ijaykishore59/resume-analyzer.git
cd resume-analyzer
