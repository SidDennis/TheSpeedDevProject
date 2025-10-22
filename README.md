# TheSpeedDevProject

This is a full-stack web application built with modern technologies.

## Features

- FastAPI backend with MongoDB and Redis
- React frontend with modern UI
- Docker containerization for easy development
- Beautiful, responsive design

## Tech Stack

### Backend
- **Python 3.11+** - Programming language
- **FastAPI** - Modern, fast web framework
- **MongoDB** - NoSQL database
- **Redis** - In-memory data store for caching
- **Motor** - Async MongoDB driver
- **Pydantic** - Data validation

### Frontend
- **React 18** - JavaScript library for building user interfaces
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client
- **Lucide React** - Beautiful icons

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TheSpeedDevProject
   ```

2. **Start all services**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 🐳 Docker Commands & Demonstrations

### Essential Docker Commands

#### **Starting the Application**
```bash
# Start all services in the background
docker-compose up -d

# Start with logs visible (recommended for first run)
docker-compose up

# Start specific services only
docker-compose up -d backend frontend
```

#### **Stopping the Application**
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (clears database data)
docker-compose down -v

# Stop specific services
docker-compose stop backend
```

#### **Viewing Logs**
```bash
# View logs from all services
docker-compose logs -f

# View logs from specific service
docker-compose logs -f backend
docker-compose logs -f frontend

# View last 50 lines of logs
docker-compose logs --tail=50 backend
```

#### **Managing Services**
```bash
# Check running containers
docker-compose ps

# Restart a specific service
docker-compose restart backend
docker-compose restart frontend

# Rebuild and restart services
docker-compose up -d --build

# View resource usage
docker stats
```

### 🎯 **Step-by-Step Docker Demo**

#### **1. First Time Setup**
```bash
# Navigate to project directory
cd TheSpeedDevProject

# Start all services (this will download images on first run)
docker-compose up -d

# Wait for services to be ready (about 30 seconds)
sleep 30

# Check if all services are running
docker-compose ps
```

#### **2. Verify Everything is Working**
```bash
# Test backend health
curl http://localhost:8000/health

# Test frontend (should return HTML)
curl -I http://localhost:3000

# View API documentation
open http://localhost:8000/docs
```

#### **3. Development Workflow**
```bash
# View logs while developing
docker-compose logs -f

# Restart backend after code changes
docker-compose restart backend

# Restart frontend after CSS/JS changes
docker-compose restart frontend
```

#### **4. Clean Shutdown**
```bash
# Stop all services
docker-compose down

# Clean up everything (including volumes)
docker-compose down -v --remove-orphans
```

### 🔧 **Troubleshooting Docker Issues**

#### **Port Already in Use**
```bash
# Check what's using the ports
lsof -i :3000
lsof -i :8000

# Kill processes using the ports
sudo kill -9 $(lsof -t -i:3000)
sudo kill -9 $(lsof -t -i:8000)
```

#### **Container Won't Start**
```bash
# Check container logs
docker-compose logs backend
docker-compose logs frontend

# Rebuild containers
docker-compose down
docker-compose up -d --build --force-recreate
```

#### **Database Issues**
```bash
# Reset database (removes all data)
docker-compose down -v
docker-compose up -d

# Access MongoDB directly
docker-compose exec mongodb mongosh
```

#### **Memory Issues**
```bash
# Clean up Docker resources
docker system prune -a

# Check disk usage
docker system df
```

### 📊 **Monitoring Your Application**

#### **Real-time Monitoring**
```bash
# Monitor all containers
docker-compose logs -f

# Monitor specific service
docker-compose logs -f backend | grep ERROR

# Check container status
docker-compose ps
```

#### **Performance Monitoring**
```bash
# View resource usage
docker stats

# Check container health
docker-compose exec backend curl http://localhost:8000/health
docker-compose exec frontend curl http://localhost:3000
```

### 🚀 **Production-like Setup**

#### **Environment Variables**
```bash
# Copy environment template
cp backend/env.example backend/.env

# Edit environment variables
nano backend/.env

# Restart with new environment
docker-compose restart backend
```

#### **Data Persistence**
```bash
# View volume information
docker volume ls

# Backup database
docker-compose exec mongodb mongodump --out /data/backup

# Restore database
docker-compose exec mongodb mongorestore /data/backup
```

### 🎉 **Quick Demo Script**

Create a file called `demo.sh`:
```bash
#!/bin/bash
echo "🚀 TheSpeedDevProject Docker Demo"
echo "================================"

echo "📦 Starting services..."
docker-compose up -d

echo "⏳ Waiting for services to be ready..."
sleep 15

echo "🔍 Checking service status..."
docker-compose ps

echo "🧪 Testing endpoints..."
curl -s http://localhost:8000/health | jq
curl -s -I http://localhost:3000 | head -1

echo "🌐 Your application is ready!"
echo "   Frontend: http://localhost:3000"
echo "   Backend:  http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
```

Make it executable and run:
```bash
chmod +x demo.sh
./demo.sh
```

### Local Development

#### Backend Setup

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
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env file with your configuration
   ```

5. **Start MongoDB and Redis**
   ```bash
   # Using Docker
   docker run -d -p 27017:27017 --name mongodb mongo:7.0
   docker run -d -p 6379:6379 --name redis redis:7.2-alpine
   ```

6. **Run the backend**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

#### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

## API Endpoints

### Users
- `GET /api/v1/users` - Get all users
- `GET /api/v1/users/{user_id}` - Get user by ID
- `POST /api/v1/users` - Create new user
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user

### Health Check
- `GET /health` - API health status

## Project Structure

```
TheSpeedDevProject/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── routers/
│   │       ├── __init__.py
│   │       └── users.py
│   ├── requirements.txt
│   ├── env.example
│   └── Dockerfile
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── index.css
│   ├── package.json
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Features

### Backend Features
- ✅ FastAPI with automatic API documentation
- ✅ MongoDB integration with Motor async driver
- ✅ Redis caching for improved performance
- ✅ Pydantic models for data validation
- ✅ CORS configuration for frontend integration
- ✅ Error handling and validation
- ✅ Async/await support throughout

### Frontend Features
- ✅ Modern React 18 with hooks
- ✅ Beautiful UI with Tailwind CSS
- ✅ Responsive design for all devices
- ✅ User management (CRUD operations)
- ✅ Modal forms for user creation/editing
- ✅ Loading states and error handling
- ✅ Clean, intuitive interface

## Development

### Adding New Features

1. **Backend**: Add new routers in `app/routers/`
2. **Frontend**: Create new components in `src/components/`
3. **Database**: Update models in `app/models.py`

### Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## Deployment

### Production Docker Setup

1. **Build production images**
   ```bash
   docker-compose -f docker-compose.prod.yml build
   ```

2. **Deploy with production configuration**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Authors**: Siddharth Dennis and Jacky Shen
