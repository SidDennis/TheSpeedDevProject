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

## 🐳 Docker Commands

### Essential Docker Commands

```bash
# Build the containers
docker-compose build

# Start all services
docker-compose up -d

# Stop all services
docker-compose down
```

### Quick Demo

```bash
# Build and start everything
docker-compose up -d --build

# Check if services are running
docker-compose ps

# View logs
docker-compose logs -f

# Stop everything
docker-compose down
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
