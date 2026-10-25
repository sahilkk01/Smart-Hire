
def generate_suggestions(missing_skills):
    suggestions = []

    learning_resources = {
        "Python": "Practice Python functions, loops, and projects.",
        "Flask": "Build a small Flask web application.",
        "SQL": "Practice SQL queries, joins, and database operations.",
        "MySQL": "Create a database and practise CRUD operations.",
        "HTML": "Practise semantic HTML and forms.",
        "CSS": "Build responsive layouts using Flexbox and Grid.",
        "JavaScript": "Practise DOM manipulation and event handling.",
        "React": "Learn React components, props, and state.",
        "Git": "Practise commits, branches, and version control.",
        "GitHub": "Upload a project with a clear README.",
        "Machine Learning": "Build a beginner machine learning project.",
        "Pandas": "Practise cleaning and analysing datasets.",
        "NumPy": "Practise arrays and numerical operations.",
        "Excel": "Learn formulas, sorting, filtering, and pivot tables.",
        "Tableau": "Create a dashboard using a sample dataset.",
        "Bootstrap": "Build a responsive page using Bootstrap.",
        "REST API": "Build and test a simple REST API.",
        "Django": "Build a small Django application.",
        "Data Analysis": "Complete a data analysis project."
    }

    for skill in missing_skills:
        suggestion = learning_resources.get(skill)

        if suggestion:
            suggestions.append({
                "skill": skill,
                "suggestion": suggestion
            })
        else:
            suggestions.append({
                "skill": skill,
                "suggestion": (
                    "Study this skill and practise it with a relevant project."
                )
            })

    if not suggestions:
        suggestions.append({
            "skill": "Resume",
            "suggestion": (
                "No missing skills were detected in our current skill list. "
                "Review your project descriptions and job-specific experience."
            )
        })

    return suggestions
