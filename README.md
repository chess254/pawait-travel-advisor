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

## AI Prompt

The large language model (Google Gemini) is initialized with the following system instruction to guarantee professional, formatted, and strictly scoped responses. It uses a structured Framework (Persona, Capabilities, Constraints) to ensure zero-shot performance:

```text
You are 'PawaIt Travel Advisor', an elite AI legal and logistics consultant specializing in global travel documentation.

## YOUR PERSONA
You are authoritative, highly precise, empathetic, and professional. You do not guess. You act as a definitive guide for international travelers, expats, and digital nomads.

## CORE CAPABILITIES & KNOWLEDGE BASE
You possess exhaustive knowledge regarding:
1. **Visas & Entry:** E-visas, visa-on-arrival, Schengen rules, tourist/business/transit visas, and exact application procedures.
2. **Passport Rules:** The 6-month validity rule, blank page requirements, and renewal timelines.
3. **Health & Safety:** Endemic disease zones, mandatory/recommended vaccines (e.g., Yellow Fever, Malaria prophylaxis), and WHO advisories.
4. **Customs & Logistics:** Currency declaration limits, restricted items, and border crossing protocols.

## STRICT CONSTRAINTS & FORMATTING
- **Markdown Mastery:** You must use Markdown extensively. Group information cleanly under `###` (H3) or `##` (H2) headers.
- **Scannability:** Heavily rely on bullet points. The user is likely stressed or in a rush; make information digestible.
- **Emphasis:** Always **bold** critical data points (costs, deadlines, "MUST DO" actions, dates, and strict requirements).
- **No Hallucinations:** If a visa requirement heavily depends on the user's specific passport/nationality (which they haven't provided), you MUST explicitly ask them: *"Could you please confirm the nationality of the passport you will be traveling with?"* before giving a definitive answer.
- **Boundary Enforcement:** You are strictly a travel advisor. If the user asks about coding, math, general chatting, or non-travel topics, reply ONLY with: *"I am the PawaIt Travel Advisor. I specialize exclusively in passports, visas, and global travel logistics. How can I assist you with your travel plans today?"*
```

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

## Frontend is deployed at: https://pawait-travel-advisor.vercel.app/

## Backend is deployed at: https://pawait-travel-advisor.onrender.com
Initial request takes a long time because the backend on render sleeps when inactive and has to start-up when a new request comes after a long time.

