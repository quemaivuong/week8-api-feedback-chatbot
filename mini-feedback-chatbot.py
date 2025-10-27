import requests
import random
import json
import sys

# === STEP 1: Fake student answer ===
# Provide interactive input with defaults so a user can type their own text when running the script.
default_answer = "The movie was good."
default_keyword = "good"
# If running in an interactive terminal, prompt the user; otherwise (non-interactive run) use defaults.
if sys.stdin is not None and sys.stdin.isatty():
    try:
        student_answer = input(f'Enter student answer (press Enter to use default: "{default_answer}"): ').strip() or default_answer
        keyword = input(f'Enter focus word to improve (press Enter to use default: "{default_keyword}"): ').strip() or default_keyword
    except EOFError:
        # Unexpected EOF while reading input -> fall back to defaults
        student_answer = default_answer
        keyword = default_keyword
else:
    # Non-interactive environment (e.g., running from an automation or this terminal runner) -> use defaults
    student_answer = default_answer
    keyword = default_keyword

# === STEP 2: Get synonyms using Datamuse API ===
def get_synonyms(word):
    url = f"https://api.datamuse.com/words?rel_syn={word}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return [item["word"] for item in data[:5]]  # top 5 synonyms
    except requests.RequestException:
        # Network error, timeout, or non-200 status -> return empty list fallback
        return []

# === STEP 3: Get motivational quote from Quotable ===
def get_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return f"“{data['content']}” — {data['author']}"
    except requests.RequestException:
        # If the API isn't reachable, provide a safe fallback quote
        return "Keep learning and improving!"

# === STEP 4: Get word definition from Free Dictionary ===
def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        try:
            return data[0]["meanings"][0]["definitions"][0]["definition"]
        except (KeyError, IndexError, TypeError):
            return "No definition found."
    except requests.RequestException:
        # Network error, timeout, or non-200 status -> return fallback
        return "Unable to fetch definition."

# === STEP 5: Generate feedback ===
synonyms = get_synonyms(keyword)
quote = get_quote()
definition = get_definition(keyword)

# pick a random synonym for a concrete suggestion (falls back to the original word)
selected_synonym = random.choice(synonyms) if synonyms else keyword

feedback = {
    "student_answer": student_answer,
    "focus_word": keyword,
    "synonyms": synonyms,
    "definition": definition,
    "motivational_quote": quote,
    "suggested_feedback": (
        f"Your sentence is clear! You could replace '{keyword}' with '{selected_synonym}' or one of these "
        f"words for richer expression: {', '.join(synonyms)}. "
        f"The word '{keyword}' means: {definition}. "
        f"Keep it up! {quote}"
    )
}

# === STEP 6: Print and save to JSON ===
print("\n--- Personalized Feedback ---")
print(feedback["suggested_feedback"])

with open("student_feedback.json", "w", encoding="utf-8") as f:
    json.dump(feedback, f, indent=2, ensure_ascii=False)

print("\n✅ Feedback saved to student_feedback.json")
