from flask import Flask, render_template, request
from utils.scorer import evaluate_resume

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    if 'resume' not in request.files or request.files['resume'].filename == '':
        return "No resume uploaded", 400

    resume_file = request.files['resume']
    job_desc = request.form.get("job_desc")

    score, feedback, suggestions = evaluate_resume(resume_file, job_desc)

    return render_template("result.html", score=score, feedback=feedback, suggestions=suggestions)


if __name__ == "__main__":
    app.run(debug=True)




