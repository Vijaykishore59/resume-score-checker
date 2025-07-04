import PyPDF2
import re
import spacy
import textstat
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join([page.extract_text() or '' for page in reader.pages])

def clean_text(text):
    return re.sub(r'\s+', ' ', text.strip().lower())
def evaluate_resume(file, job_desc):
    text = extract_text_from_pdf(file)
    cleaned_text = clean_text(text)
    cleaned_job = clean_text(job_desc)

    score = 0
    feedback = []
    suggestions = []

    # Keyword Match
    vectorizer = TfidfVectorizer().fit([cleaned_job])
    job_vec = vectorizer.transform([cleaned_job])
    resume_vec = vectorizer.transform([cleaned_text])
    similarity = (resume_vec @ job_vec.T).toarray()[0][0]
    score += similarity * 50
    feedback.append(f"Keyword match: {similarity:.2f}")

    if similarity < 0.2:
        suggestions.append("Include more keywords from the job description to improve your match.")

    # Readability Score
    readability = textstat.flesch_reading_ease(cleaned_text)
    score += min(readability, 100) * 0.3
    feedback.append(f"Readability: {readability:.2f}")

    if readability < 40:
        suggestions.append("Simplify your language and sentence structure for better readability.")

    # Section Check
    for section in ['education', 'experience', 'skills', 'projects']:
        if section in cleaned_text:
            score += 5
            feedback.append(f"✓ Section present: {section}")
        else:
            feedback.append(f"✗ Missing section: {section}")
            suggestions.append(f"Add a section for {section} — it's essential for hiring managers.")

    # Bonus: Check for weak language
    if not any(verb in cleaned_text for verb in ['managed', 'led', 'created', 'built', 'developed']):
        suggestions.append("Use strong action verbs like 'led', 'built', or 'managed' to showcase your impact.")

    return round(min(score, 100), 2), feedback, suggestions
