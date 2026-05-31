# 🚀 Setup Guide - All-Lucky-ai

## Prerequisites

- Python 3.9+
- Node.js 16+
- FFmpeg
- NVIDIA GPU (RTX 3060 or better recommended)
- 100GB+ storage

## Environment Setup

### 1. Backend Setup

```bash
# Clone repository
git clone https://github.com/myai8541/All-Lucky-ai.git
cd All-Lucky-ai/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env and add your API keys
# RUNWAY_ML_API_KEY
# OPENAI_API_KEY
# HUGGINGFACE_API_KEY

# Start the backend
uvicorn main:app --reload
```

### 2. Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install

# Copy environment template
cp .env.example .env

# Start development server
npm start
```

### 3. Database Setup

```bash
# Using Docker
docker-compose up postgres redis

# Or install PostgreSQL locally
```

## API Keys Configuration

### Runway ML
1. Visit: https://app.runwayml.com
2. Sign up and create API key
3. Add to `.env`: `RUNWAY_ML_API_KEY=your_key`

### OpenAI
1. Visit: https://platform.openai.com/api-keys
2. Create API key
3. Add to `.env`: `OPENAI_API_KEY=your_key`

### Hugging Face
1. Visit: https://huggingface.co/settings/tokens
2. Create API token
3. Add to `.env`: `HUGGINGFACE_API_KEY=your_key`

## Verify Installation

```bash
# Backend health check
curl http://localhost:8000/health

# Frontend
Open http://localhost:3000
```

## Troubleshooting

### GPU Not Detected
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

### FFmpeg Not Found
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
choco install ffmpeg
```

### Database Connection Error
Check PostgreSQL is running: `psql --version`

---

For more help, check GitHub Issues!
