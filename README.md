# PawaIt AI Travel Assistant

A modern full-stack web application that serves as an interactive Q&A system for travel-related documentation and advisories.

## Tech Stack

- **Frontend**: Next.js (App Router), TypeScript, TailwindCSS, Framer Motion
- **Backend**: FastAPI (Python), pydantic-settings, Google Gemini AI integration
- **Styling**: Modern, responsive design with glassmorphism and smooth animations
- **Infrastructure**: Docker, Docker Compose, GitHub Actions CI

## Features

- **Real-time AI Responses**: Integrated with Google Gemini for accurate travel advice.
- **Modern UI**: Clean, professional interface with loading states and markdown support.
- **Modular Architecture**: Clean separation of concerns with frontend custom hooks and backend modular routers/services.
- **Type Safety**: End-to-end type safety using TypeScript on the frontend and MyPy on the backend.
- **Automated CI/CD**: GitHub Actions workflows for continuous integration testing and linting.
- **Containerized**: Fully Dockerized for seamless development and deployment.

## Project Structure

### Backend
The backend follows a standard FastAPI structure for modularity and scalability:
- `app/api/routers/`: Endpoint definitions (health, chat)
- `app/core/`: Configuration and settings
- `app/schemas/`: Pydantic models for validation
- `app/services/`: Core logic and third-party integrations (Gemini AI)

### Frontend
The frontend separates UI and data-fetching concerns:
- `src/components/`: Reusable React components
- `src/hooks/`: Custom state-management hooks (`useChat`)
- `src/services/`: API client wrappers

---

## Quick Start (Docker - Recommended)

The easiest way to run the application is using Docker Compose.

1. Create a `.env` in the `backend` directory with your Gemini API Key:
   ```env
   GEMINI_API_KEY=your_key_here
   ```
2. From the root directory, start the containers:
   ```bash
   docker-compose up --build
   ```

The Frontend will be available at `http://localhost:3000` and the Backend API at `http://localhost:8000`.

---

## Manual Setup

### Prerequisites

- Python 3.10+
- Node.js 20+
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your API key:
   ```env
   GEMINI_API_KEY=your_key_here
   ```
5. Run the server:
   ```bash
   python run.py
   ```

*(Developer tools like Ruff and MyPy are included for linting and type checking).*

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm ci
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

---

## API Documentation

Once the backend is running, you can access the Swagger documentation at:
`http://localhost:8000/docs`

