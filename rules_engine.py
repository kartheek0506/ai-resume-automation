def decide_action(ai_result):
    confidence = ai_result["confidence"]
    category = ai_result["category"]

    if category == "Shortlisted" and confidence >= 0.75:
        return "Send interview invitation email"
    elif category == "Needs Review":
        return "Send manual review notification"
    else:
        return "Send rejection email"
