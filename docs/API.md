# 📚 API Documentation - All-Lucky-ai

## Base URL
```
http://localhost:8000/api
```

## Authentication
All endpoints (except health check) require JWT token:
```
Authorization: Bearer <your_jwt_token>
```

## Endpoints

### 1. Health Check
```
GET /health
```
Response:
```json
{
  "status": "healthy",
  "service": "All-Lucky-ai"
}
```

### 2. Text-to-Video Generation
```
POST /v1/generate/text-to-video
```

Request:
```json
{
  "prompt": "एक सुंदर सूर्यास्त समुद्र के किनारे...",
  "duration": 30,
  "style": "cinematic",
  "quality": "1080p",
  "fps": 30
}
```

Response:
```json
{
  "job_id": "uuid-string",
  "status": "processing",
  "created_at": "2024-01-01T00:00:00Z"
}
```

### 3. Image-to-Video Generation
```
POST /v1/generate/image-to-video
```

Request:
```json
{
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ],
  "duration": 30,
  "transition": "smooth",
  "fps": 30
}
```

Response:
```json
{
  "job_id": "uuid-string",
  "status": "processing",
  "created_at": "2024-01-01T00:00:00Z"
}
```

### 4. Audio-to-Video Generation
```
POST /v1/generate/audio-to-video
```

Request:
```json
{
  "audio_url": "https://example.com/audio.mp3",
  "style": "animated",
  "duration": 30,
  "quality": "1080p"
}
```

Response:
```json
{
  "job_id": "uuid-string",
  "status": "processing",
  "created_at": "2024-01-01T00:00:00Z"
}
```

### 5. Get Job Status
```
GET /v1/jobs/{job_id}
```

Response:
```json
{
  "job_id": "uuid-string",
  "status": "completed",
  "progress": 100,
  "video_url": "https://storage.example.com/video.mp4",
  "created_at": "2024-01-01T00:00:00Z",
  "completed_at": "2024-01-01T00:45:00Z"
}
```

### 6. List Jobs
```
GET /v1/jobs?skip=0&limit=10
```

Response:
```json
{
  "total": 50,
  "jobs": [
    {
      "job_id": "uuid-string",
      "status": "completed",
      "type": "text-to-video",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

## Status Values
- `queued` - Job in queue
- `processing` - Currently processing
- `completed` - Successfully completed
- `failed` - Processing failed
- `cancelled` - Job was cancelled

## Error Responses

```json
{
  "detail": "Error message",
  "status_code": 400
}
```

## Rate Limiting
- 100 requests per minute per IP
- Max 10 concurrent jobs per user

---

For interactive documentation, visit: `http://localhost:8000/docs`
