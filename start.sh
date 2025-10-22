#!/bin/bash

echo "🚀 Starting TheSpeedDevProject..."
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

echo "📦 Building and starting all services..."
docker-compose up -d --build

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

echo ""
echo "✅ Services are starting up!"
echo ""
echo "🌐 Access your application:"
echo "   Frontend:    http://localhost:3000"
echo "   Backend API: http://localhost:8000"
echo "   API Docs:    http://localhost:8000/docs"
echo ""
echo "📊 To view logs:"
echo "   docker-compose logs -f"
echo ""
echo "🛑 To stop services:"
echo "   docker-compose down"
echo ""
echo "🎉 Happy coding!"
