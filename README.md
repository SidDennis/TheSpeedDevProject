# TheSpeedDevProject

A full-stack web application with FastAPI backend and React frontend.

## 🚀 Quick Start - Backend Testing

### Prerequisites
- Docker and Docker Compose
- Python 3.11+ (for local development)
- curl or any API testing tool

### Method 1: Using Docker (Recommended)

1. **Start the backend service only**
   ```bash
   docker-compose up backend -d
   ```

2. **Test the API endpoints**
   ```bash
   # Test the root endpoint
   curl http://localhost:8000/
   
   # Expected response: {"message": "Hello World"}
   ```

3. **View API documentation**
   - Open browser: http://localhost:8000/docs
   - Interactive Swagger UI for testing endpoints

4. **Check service status**
   ```bash
   docker-compose ps
   docker-compose logs backend
   ```

### Method 2: Local Development

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the backend server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Test the API**
   ```bash
   curl http://localhost:8000/
   ```

## 🧪 Backend Testing Guide

### Available Endpoints

| Method | Endpoint | Description | Expected Response |
|--------|----------|-------------|------------------|
| GET | `/` | Root endpoint | `{"message": "Hello World"}` |
| GET | `/docs` | API documentation | Swagger UI interface |
| GET | `/redoc` | Alternative docs | ReDoc interface |

### Testing Commands

```bash
# Test root endpoint
curl http://localhost:8000/

# Test with verbose output
curl -v http://localhost:8000/

# Test with JSON formatting
curl http://localhost:8000/ | jq

# Test API documentation
curl http://localhost:8000/docs
```

### Using Browser Testing

1. **Root endpoint**: http://localhost:8000/
2. **Interactive API docs**: http://localhost:8000/docs
3. **Alternative docs**: http://localhost:8000/redoc

### Using Postman/Insomnia

1. Create new request
2. Set method to `GET`
3. Set URL to `http://localhost:8000/`
4. Send request
5. Expected response: `{"message": "Hello World"}`

## 🔧 Development Commands

### Docker Commands

```bash
# Start only backend
docker-compose up backend -d

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f backend

# Stop services
docker-compose down

# Rebuild and start
docker-compose up -d --build
```

### Local Development Commands

```bash
# Install dependencies
pip install fastapi uvicorn

# Run with auto-reload
uvicorn app.main:app --reload

# Run on specific host/port
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run in production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 📁 Current Project Structure

```
TheSpeedDevProject/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py          # Main FastAPI application
│   ├── demo-app/           # Original demo (not used)
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/               # Skeleton frontend (not used for backend testing)
├── docker-compose.yml
└── README.md
```

## 🐛 Troubleshooting

### Common Issues

1. **Port 8000 already in use**
   ```bash
   # Find process using port 8000
   lsof -i :8000
   
   # Kill the process
   kill -9 <PID>
   ```

2. **Docker container not starting**
   ```bash
   # Check container logs
   docker-compose logs backend
   
   # Rebuild container
   docker-compose up -d --build backend
   ```

3. **Python module not found**
   ```bash
   # Make sure you're in the backend directory
   cd backend
   
   # Install dependencies
   pip install fastapi uvicorn
   ```

### Health Checks

```bash
# Check if backend is running
curl http://localhost:8000/

# Check Docker container status
docker-compose ps

# Check container logs
docker-compose logs backend
```

## 🎯 Next Steps

Once the backend is working:

1. **Add new endpoints** in `app/main.py`
2. **Test endpoints** using curl or browser
3. **Use interactive docs** at http://localhost:8000/docs
4. **Build frontend integration** when ready

## 📚 Useful Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [curl Manual](https://curl.se/docs/manual.html)

---

**Happy coding!** 🚀