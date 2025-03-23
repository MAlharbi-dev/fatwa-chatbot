# AI-Powered Fatwa Chatbot 

## Overview
This project is an **AI-powered Fatwa Chatbot** that helps users get Islamic rulings based on a database of fatwas from trusted scholars. It uses **Natural Language Processing (NLP)** to understand user queries and find relevant answers.

---

## Features
✅ **User-friendly Chat Interface** – Ask Islamic questions in Arabic.  
✅ **AI-Powered Search** – Finds relevant fatwas using NLP techniques.  
✅ **Fatwa Database** – Stores rulings from trusted scholars.  
✅ **Django Backend** – Handles user requests and retrieves answers.  
✅ **Secure & Fast** – Uses MySQL for efficient data handling.  

---

## Tech Stack  
| Component     | Technology Used |
|--------------|----------------|
| **Backend**  | Django (Python) |
| **Frontend** | HTML, CSS, JavaScript, jQuery |
| **Database** | MySQL |
| **AI/NLP**   | NLTK, SpaCy, TF-IDF |
| **Model**    | LSTM-based encoder |

---

## Setup Instructions  

### 1. Clone the Repository  

git clone https://github.com/YOUR_USERNAME/fatwa-chatbot.git
cd fatwa-chatbot

### 2 Create a Virtual Environment & Activate it
sh
Copy
Edit
python3 -m venv env  
source env/bin/activate   # For Mac & Linux
### 3. Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
### 4. Set Up the Database
sh
Copy
Edit
python manage.py migrate
### 5. Run the Server
sh
Copy
Edit
python manage.py runserver
### Open http://127.0.0.1:8000/ in your browser.


# fatwa-chatbot
