
from flask import Flask, render_template, request, redirect, url_for

from database import (
    save_analysis,
    get_history,
    delete_history,
    clear_all_history
)

from scraper.job_scraper import extract_job_text
from resume.resume_parser import extract_resume_text
from matcher.skill_matcher import compare_skills
from scraper.job_parser import extract_job_details
from matcher.recommendations import generate_suggestions


app = Flask(__name__)

# Maximum uploaded file size: 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "GET":
        return render_template("index.html", job_url="")

    # Get job URL
    job_url = request.form.get("job_url", "").strip()

    if not job_url:
        return render_template(
            "index.html",
            job_url="",
            error="Please enter a job posting URL."
        )

    # Get resume file
    resume_file = request.files.get("resume_file")

    if not resume_file or not resume_file.filename:
        return render_template(
            "index.html",
            job_url=job_url,
            resume_error="Please upload your resume."
        )

    if not resume_file.filename.lower().endswith(".pdf"):
        return render_template(
            "index.html",
            job_url=job_url,
            resume_error="Please upload a PDF file."
        )

    # Extract job description
    try:
        job_text = extract_job_text(job_url)

        if not job_text or not job_text.strip():
            return render_template(
                "index.html",
                job_url=job_url,
                error="No readable job text was found."
            )

    except Exception:
        return render_template(
            "index.html",
            job_url=job_url,
            error="Could not extract the job details. Please check the link."
        )

    # Extract resume text
    try:
        resume_text = extract_resume_text(resume_file.stream)

        if not resume_text or not resume_text.strip():
            return render_template(
                "index.html",
                job_url=job_url,
                resume_error="No readable text found in the PDF."
            )

    except Exception:
        return render_template(
            "index.html",
            job_url=job_url,
            resume_error="Could not read this PDF."
        )

    # Compare job and resume skills
    (
        matched_skills,
        missing_skills,
        match_score,
        job_skills
    ) = compare_skills(job_text, resume_text)

    # Extract job requirements
    job_details = extract_job_details(job_text)

    # Generate resume improvement suggestions
    suggestions = generate_suggestions(missing_skills)

    # Save analysis in SQLite
    save_analysis(
        job_url,
        match_score,
        matched_skills,
        missing_skills
    )

    # Show the separate results page
    return render_template(
        "results.html",
        job_url=job_url,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        job_skills=job_skills,
        match_score=match_score,
        job_details=job_details,
        suggestions=suggestions
    )


@app.route("/history")
def history_page():
    history = get_history()
    return render_template("history.html", history=history)


# Database link: open saved analysis records
@app.route("/database")
def database_page():
    records = get_history()
    return render_template("database.html", records=records)


@app.route("/delete-history/<int:history_id>", methods=["POST"])
def delete_history_page(history_id):
    delete_history(history_id)
    return redirect(url_for("history_page"))


@app.route("/clear-history", methods=["POST"])
def clear_history_page():
    clear_all_history()
    return redirect(url_for("history_page"))


if __name__ == "__main__":
    app.run(debug=True)
