
import re


def extract_job_details(job_text):
    text = job_text.lower()

    # Extract recognized skills
    skills = [
        "Python", "Flask", "Django", "HTML", "CSS",
        "JavaScript", "React", "SQL", "MySQL", "Git",
        "Machine Learning", "Pandas", "NumPy",
        "Excel", "Tableau", "Bootstrap", "REST API"
    ]

    required_skills = []

    for skill in skills:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, text):
            required_skills.append(skill)

    # Find education-related text
    education = []

    education_keywords = [
        "bachelor", "b.tech", "btech", "degree",
        "computer science", "graduation"
    ]

    for keyword in education_keywords:
        if keyword in text:
            education.append(keyword)

    # Find experience-related text
    experience = []

    experience_patterns = [
        r"\d+\+?\s*years?\s+of\s+experience",
        r"fresher",
        r"entry.level",
        r"internship"
    ]

    for pattern in experience_patterns:
        matches = re.findall(pattern, text)

        for match in matches:
            experience.append(match)

    return {
        "required_skills": required_skills,
        "education": education,
        "experience": experience
    }
