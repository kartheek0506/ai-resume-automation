from ai_classifier import classify_resume
from rules_engine import decide_action

with open("resumes/sample_resume.txt", "r") as file:
    resume_text = file.read()

ai_result = classify_resume(resume_text)
action = decide_action(ai_result)

print("AI Result:", ai_result)
print("Automation Action:", action)
