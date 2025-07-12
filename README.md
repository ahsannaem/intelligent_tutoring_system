#  Intelligent Tutoring System (ITS)

The **Intelligent Tutoring System (ITS)** is a personalized, AI-powered web application that adapts learning content based on student performance. Built using Django and integrated with a machine learning model, it provides a dynamic educational experience where students are assessed through quizzes, classified based on proficiency, and recommended appropriate study material to improve effectively.

---

## Key Features

- 🔐 **Student Login System** – Secure authentication using Django's built-in auth system.
- 📝 **Quiz Engine** – Structured quizzes to assess student understanding.
- 📊 **ML-Based Classification** – Classify students (e.g., beginner, intermediate, advanced) using a trained machine learning model.
- 🎯 **Personalized Content Routing** – Recommend study material based on the student’s predicted proficiency level.
- 🧾 **Progress Dashboard** – Track user quiz history, badges, and learning progress.
- 📚 **Study Materials** – Dynamically served based on performance and improvement needs.

---

## Project Structure

its-v1/
```bash
│
├── accounts/ # Handles user profiles, registration, login, etc.
├── quiz/ # Quiz logic, models, forms, views, grading
├── its/ # Django project-level config (settings, urls)
├── static/ # JS, CSS, ML model, and images
├── templates/ # HTML templates for UI
├── media/ # Uploaded files (if any)
├── scripts/ # Custom utilities or migration helpers
│
├── db.sqlite3 # Default development database
├── manage.py # Django management script
├── import_csv.py # Script to load quizzes from CSV
├── req.txt # Python dependencies
└── README.md # You are here!
```

## ⚙️ Setup Instructions

###  Prerequisites

- Python 3.10 or higher
- `virtualenv` installed (`pip install virtualenv`)
- Git (optional)

---

### 🔧 Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ahsannaem/intelligent_tutoring_system.git
   cd its-v1

### Create and Activate a Virtual Environment
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

### Install Dependencies
    ```bash
    pip install --upgrade pip
    pip install -r req.txt
    ```


### Apply Migrations
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### Create a Superuser (optional)
    ```bash
    python manage.py createsuperuser
    ```

### Run Server
    ```bash
    py manage.py runserver
    ```
### Open your browser and visit: http://localhost:8000

Machine Learning Integration
Located at: static/scripts/linear_regression_model.pkl
The model evaluates quiz performance and classifies the student into levels (e.g., beginner, intermediate, advanced).
This classification is used to: 
1. Adjust the difficulty of future quizzes.

2. Recommend relevant study materials.

3. Update the student dashboard with tailored feedback.

## Testing the System
You can preload quiz data using the provided fixtures:
python manage.py loaddata quiz/fixtures/data.json

Or import from CSV:
python import_csv.py


How It Works (Flow)
1. Student logs into the system.
2. A quiz is assigned based on current progress.
3. Quiz results are passed to a machine learning model.
4. Student is assigned a performance class (e.g., Level 1, 2, 3).
5. Based on the result, recommended study materials are shown.
6. The dashboard is updated with performance stats, badges, and suggestions.

Technologies Used
Backend: Django (Python)
Frontend: HTML5, CSS3, JavaScript (vanilla)
Database: SQLite (default), can be swapped with PostgreSQL
ML Integration: scikit-learn (trained model stored in .pkl)
Others: Pandas, NumPy.


## Future Improvements
-Gamification (leaderboards, streaks, levels)
-Visual analytics dashboard
-Interactive video content with embedded questions
-Admin analytics for class-level insights


Author
Ahsan
