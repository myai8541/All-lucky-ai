# 🎬 All-Lucky-ai - AI Long Video Generator

**Generate 30-minute long videos from Text, Images, and Audio using AI**

## 🚀 Features

✅ **Text-to-Video Generation** - टेक्स्ट डिस्क्रिप्शन से विडियो बनाएं
✅ **Image-to-Video** - इमेज सीक्वेंस को animated विडियो में बदलें
✅ **Audio-to-Video** - ऑडियो/वॉइस से विडियो जेनरेट करें
✅ **Real-time Preview** - लाइव प्रीव्यू देखें
✅ **Custom Styles** - विभिन्न स्टाइल और effects
✅ **Multiple Formats** - MP4, WebM, AVI support
✅ **Long Duration** - 30 मिनट तक की विडियो
✅ **Web Interface** - आसान user interface

## 📋 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Runway ML API** - Video generation
- **Stable Diffusion** - Image generation
- **OpenAI API** - Text processing
- **FFmpeg** - Video processing
- **PostgreSQL** - Database
- **Redis** - Caching

### Frontend
- **React** - UI framework
- **Tailwind CSS** - Styling
- **Axios** - API calls
- **Redux** - State management

## 🛠️ Installation & Setup

### Prerequisites
```bash
Python 3.9+
Node.js 16+
FFmpeg
GPU (NVIDIA RTX recommended)
```

### Backend Setup

```bash
# Clone repository
git clone https://github.com/myai8541/All-Lucky-ai.git
cd All-Lucky-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env और अपनी API keys add करें

# Run database migrations
alembic upgrade head

# Start backend server
uvicorn main:app --reload
```

### Frontend Setup

```bash
# Install dependencies
cd frontend
npm install

# Start development server
npm start
```

## 🔑 Required API Keys

1. **Runway ML** - https://app.runwayml.com
   - Video generation के लिए

2. **OpenAI API** - https://platform.openai.com
   - Text processing के लिए

3. **Hugging Face** - https://huggingface.co
   - Stable Diffusion models के लिए

## 📁 Project Structure

```
All-Lucky-ai/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── tests/
│   ├── requirements.txt
│   ├── .env.example
│   └── alembic/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── redux/
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   ├── package.json
│   └── .env.example
├── docs/
│   ├── API.md
│   ├── SETUP.md
│   └── USAGE.md
├── docker-compose.yml
├── .gitignore
└── README.md
```

## 🎯 Usage

### 1. Text-to-Video
```bash
POST /api/generate/text-to-video
{
  "prompt": "एक सुंदर सूर्यास्त समुद्र के किनारे...",
  "duration": 30,
  "style": "cinematic"
}
```

### 2. Image-to-Video
```bash
POST /api/generate/image-to-video
{
  "images": ["url1", "url2", ...],
  "duration": 30,
  "transition": "smooth"
}
```

### 3. Audio-to-Video
```bash
POST /api/generate/audio-to-video
{
  "audio_url": "https://example.com/audio.mp3",
  "style": "animated"
}
```

## 📊 Performance

- **Processing Time:** 15-45 मिनट (30 मिनट विडियो के लिए)
- **Output Quality:** 1080p - 4K
- **GPU Memory:** 8GB+ recommended
- **Storage:** 100GB+ for cache

## 🔐 Security

- ✅ JWT Authentication
- ✅ Rate Limiting
- ✅ Input Validation
- ✅ Encrypted API Keys
- ✅ CORS Protection

## 📝 API Documentation

Complete API docs available at: `http://localhost:8000/docs`

## 🤝 Contributing

Contributions welcome! कृपया:
1. Fork करें
2. Feature branch बनाएं
3. Changes commit करें
4. Pull request भेजें

## 📄 License

MIT License - देखें LICENSE file

## 📞 Support

क्या समस्या है? GitHub Issues में report करें!

---

**Made with ❤️ by myai8541**
