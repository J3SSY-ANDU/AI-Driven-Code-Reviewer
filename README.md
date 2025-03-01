# 🚀 AI-Driven Code Reviewer

This project is an **AI-powered code reviewer** that analyzes, detects issues, and suggests improvements for Python and other programming languages. The backend is built with **FastAPI** and integrates OpenAI's API, while the frontend is a **React-based UI** for submitting and displaying reviewed code.

---

## **🔧 Setup Instructions**
Follow these steps to set up and run the project.

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/J3SSY-ANDU/AI-Driven-Code-Reviewer.git
cd AI-Driven-Code-Reviewer
```

---

## 🖥 Backend Setup (FastAPI)
1. Navigate to the backend folder:
```sh
cd backend
```
2. Create a virtual environment (optional but recommended):
```sh
python -m venv venv
```
3. Activate the virtual environment:
   - Windows (cmd/PowerShell):
   ```sh
   venv\Scripts\activate
    ```
   - Mac/Linux:
   ```sh
   source venv/bin/activate
    ```
4. Install dependencies from `requirements.txt`:
```sh
pip install -r requirements.txt
```
5. Create a `.env` file inside the `backend` folder and add your OpenAI API key:
```sh
touch .env
```
Add the following line inside `.env`:
```sh
OPENAI_API_KEY=your-api-key-here
```
6. Run the FastAPI server:
```sh
uvicorn main:app --reload
```
The backend will now be running at http://127.0.0.1:8000.

---

## 🌐 Frontend Setup (React)
1. Navigate to the frontend folder:
```sh
cd ../frontend
```
2. Install dependencies from package.json:
```sh
npm install
```
3. Start the React development server:
```sh
npm start
```
The frontend will now be running at http://localhost:3000.

---

## ✅ Features
- 🧠 AI-Powered Code Review (Detects issues, suggests improvements)
- ⚡ FastAPI Backend (Handles requests efficiently)
- 🎨 React UI (User-friendly interface to submit and view results)
- 🔒 Secure & Configurable (Uses `.env` for API key management)



