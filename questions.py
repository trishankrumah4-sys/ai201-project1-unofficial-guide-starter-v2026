"""
Your test questions.
"""

QUESTIONS = [
    {"question": "Is the housing lottery based purely on random numbers?", "expects": "credit hours"},
    {"question": "Do dining dollars roll over from spring to the following fall?", "expects": "disappears"},
    {"question": "Who do I need to talk to first if I want to appeal a grade?", "expects": "instructor"},
    {"question": "Is there a waitlist for west lot parking permits if I miss the sale window?", "expects": "no waitlist"},
    {"question": "Is the library open later during reading week than during term?", "expects": "10pm"},
]

OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended dosage of ibuprofen for a headache?",
    "How do I write a for loop in Rust?",
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
