
import re

SKILLS = [
    "Python",
    "Flask",
    "Django",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "SQL",
    "MySQL",
    "Git",
    "GitHub",
    "REST API",
    "Machine Learning",
    "Pandas",
    "NumPy",
    "Excel",
    "Tableau",
    "Bootstrap",
    "Data Analysis"
]


def find_skills(text):
    found_skills = []
    text = text.lower()

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


def compare_skills(job_text, resume_text):
    job_skills = find_skills(job_text)
    resume_skills = find_skills(resume_text)

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(job_skills) > 0:
        score = round(len(matched_skills) / len(job_skills) * 100)
    else:
        score = 0

    return matched_skills, missing_skills, score, job_skills
