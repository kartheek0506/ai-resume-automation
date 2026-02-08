def classify_resume(resume_text):
    """
    Simulated AI-based resume classification
    """

    keywords = ["python", "machine learning", "ai", "project", "internship"]
    score = 0

    text = resume_text.lower()

    for word in keywords:
        if word in text:
            score += 1

    confidence = score / len(keywords)

    if confidence >= 0.75:
        category = "Shortlisted"
    elif confidence >= 0.5:
        category = "Needs Review"
    else:
        category = "Rejected"

    return {
        "category": category,
        "confidence": round(confidence, 2),
        "reason": "Keyword-based AI evaluation"
    }
