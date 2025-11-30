# Prakriti Assessment

This project is a web-based application for determining an individual's Ayurvedic Prakriti. Prakriti is a fundamental concept in Ayurveda that represents a person's unique constitution, which is determined at the time of conception and remains constant throughout their life. There are three main types of Prakriti: Vata, Pitta, and Kapha. This application uses a questionnaire and machine learning models to assess a user's Prakriti and provide personalized recommendations.

## Features

-   Interactive questionnaire for Prakriti assessment.
-   Provides a detailed analysis of the user's Prakriti.
-   Personalized diet and lifestyle recommendations based on the Prakriti.
-   Chatbot for answering user queries.

## Technologies Used

### Frontend

-   React.js
-   Vite
-   Tailwind CSS

### Backend

-   Python
-   FastAPI
-   SQLAlchemy

### Machine Learning

-   TensorFlow/Keras
-   Scikit-learn
-   NLTK

## Project Structure

```
PrakritiAssessment/
├── dataset/              # Contains the CSV data used for training
├── frontend/             # React frontend application
│   ├── src/
│   └── ...
├── Models/               # Trained machine learning models
├── .gitignore
├── app.log               # Application log file
├── diag.py               # Main Python script for the backend
├── prakriti.db           # SQLite database
└── requirements.txt      # Python dependencies
```

## Getting Started

### Prerequisites

-   Python 3.9+
-   Node.js 18.x and npm

### Backend Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tejdeeptn7/Capstone-Project-CSE_184-.git
    cd Capstone-Project-CSE_184-/PrakritiAssessment/PrakritiAssessment
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install the dependencies:**
    ```bash
    npm install
    ```

### Running the Application

1.  **Run the backend server:**
    From the `PrakritiAssessment/PrakritiAssessment` directory, run:
    ```bash
    uvicorn diag:app --reload
    ```
    The backend will be running at `http://127.0.0.1:8000`.

2.  **Run the frontend development server:**
    From the `PrakritiAssessment/PrakritiAssessment/frontend` directory, run:
    ```bash
    npm run dev
    ```
    The frontend will be running at `http://localhost:5173`.

## Usage

1.  Open your web browser and navigate to `http://localhost:5173`.
2.  Follow the on-screen instructions to complete the questionnaire.
3.  Once you have answered all the questions, the application will display your Prakriti assessment.
4.  You can also interact with the chatbot to ask questions about Ayurveda and Prakriti.

## Dataset and Models

The machine learning models were trained on a custom dataset containing information about Prakriti. The models are located in the `Models/` directory.

-   `prakriti.keras`: A Keras model for Prakriti prediction.
-   `nlpbot.keras`: A Keras model for the chatbot.
-   `classes.pkl`, `words.pkl`: Supporting files for the models.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
