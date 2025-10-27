
# Mini Feedback Chatbot

# Mini Feedback Chatbot (Week 8 API Project)

This project was created for **EDUC 5913: Programming Fundamentals**.  
It demonstrates how to use **public APIs** to simulate AI-generated feedback for students’ writing without requiring an OpenAI key.

---

## Project Description

The chatbot takes a **student’s short answer** (e.g., “The movie was good.”) and generates a personalized feedback message.  
It uses **three free APIs** to simulate the AI feedback process:

1.  **Datamuse API** – finds synonyms to suggest richer vocabulary.  
2.  **Free Dictionary API** – gives definitions for key words.  
3.  **Quotable API** – provides motivational quotes for encouragement.  

The chatbot combines all this information into a coherent feedback message and saves it as a JSON file.

---

##  Features

- Generates feedback automatically based on a student’s sentence  
- Suggests synonyms and definitions  
- Includes motivational quotes  
- Saves results as a JSON file (`student_feedback.json`)  
- Works 100% offline once installed (no paid API keys needed)

---

## Technologies Used

- Python 3.x  
- `requests` (for making API calls)  
- `json` (for saving structured feedback)

---

## How to Run

1. **Install dependencies**  
   ```bash
   pip install requests


