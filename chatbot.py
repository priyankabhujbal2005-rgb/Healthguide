
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the health knowledge base
DATA_FILE = Path(__file__).parent / "data" / "health_faq.csv"

df = pd.read_csv(DATA_FILE).fillna("")
df["question"] = df["question"].astype(str)
df["answer"] = df["answer"].astype(str)
df["source"] = df["source"].astype(str)

# Prepare questions for matching
vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    strip_accents="unicode",
    stop_words="english"
)
question_vectors = vectorizer.fit_transform(df["question"])

# Basic warning-sign detection.
# This is a limited keyword check, not a medical assessment.
EMERGENCY_KEYWORDS = [
    "chest pain",
    "cannot breathe",
    "can't breathe",
    "difficulty breathing",
    "severe bleeding",
    "unconscious",
    "not breathing",
    "face drooping",
    "facial drooping",
    "difficulty speaking",
    "one sided weakness",
    "one-sided weakness",
    "sudden severe headache",
    "suicidal",
    "want to kill myself"
]


def get_response(user_question):
    """Return a relevant educational answer or a safe fallback."""

    if not user_question or not user_question.strip():
        return {
            "answer": "Please enter a health question.",
            "source": "",
            "status": "empty"
        }

    query = user_question.strip().lower()

    # Check for potentially urgent warning signs first
    if any(keyword in query for keyword in EMERGENCY_KEYWORDS):
        return {
            "answer": (
                "Your message may describe a medical emergency. "
                "Please contact your local emergency service or go "
                "to the nearest emergency department now. Do not delay "
                "care while using this chatbot. If you are in India, "
                "you can call 112 for emergency assistance."
            ),
            "source": "https://112.gov.in/",
            "status": "urgent"
        }

    # Match the user's question against the knowledge base
    query_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(
        query_vector, question_vectors
    ).flatten()

    best_index = similarities.argmax()
    best_score = similarities[best_index]

    # Avoid returning an unrelated answer
    if best_score < 0.30:
        return {
            "answer": (
                "Sorry, I couldn't find a suitable answer in my "
                "health knowledge base. Please try asking in a "
                "different way or consult a qualified healthcare "
                "professional for personal medical advice."
            ),
            "source": "",
            "status": "not_found"
        }

    return {
        "answer": df.iloc[best_index]["answer"],
        "source": df.iloc[best_index]["source"],
        "status": "success"
    }
