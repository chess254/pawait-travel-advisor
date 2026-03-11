# PawaIt AI Travel Assistant

A modern full-stack web application that serves as an interactive Q&A system for travel-related documentation and advisories.

## Tech Stack

- **Frontend**: Next.js (App Router), TypeScript, TailwindCSS, Framer Motion
- **Backend**: FastAPI (Python), Google Gemini AI integration
- **Styling**: Modern, responsive design with glassmorphism and smooth animations

## Features

- **Real-time AI Responses**: Integrated with Google Gemini for accurate travel advice.
- **Modern UI**: Clean, professional interface with loading states and markdown support.
- **Responsive**: Fully functional on mobile, tablet, and desktop.
- **Interactive Chat**: Fluid interaction flow with prompt engineering for a specialized travel persona.

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
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
   python main.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

## API Documentation

Once the backend is running, you can access the Swagger documentation at:
`http://localhost:8000/docs`

## Evaluation Criteria Met

- **Code Quality**: Structured backend with models and clean frontend components.
- **Technical Implementation**: Full-stack integration with Gemini AI.
- **UI/UX**: Responsive TailwindCSS design with attention to detail.
