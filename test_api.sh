#!/bin/bash

echo "🧪 Testing TheSpeedDevProject API"
echo "================================="
echo ""

# Test 1: Health Check
echo "1️⃣ Testing Health Check..."
curl -s http://localhost:8000/health | jq
echo ""

# Test 2: Root endpoint
echo "2️⃣ Testing Root Endpoint..."
curl -s http://localhost:8000/ | jq
echo ""

# Test 3: Get all users (should be empty initially)
echo "3️⃣ Testing Get All Users..."
curl -s http://localhost:8000/api/v1/users | jq
echo ""

# Test 4: Create a new user
echo "4️⃣ Testing Create User..."
USER_RESPONSE=$(curl -s -X POST http://localhost:8000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }')
echo "$USER_RESPONSE" | jq
echo ""

# Extract user ID from response
USER_ID=$(echo "$USER_RESPONSE" | jq -r '.id')
echo "Created user with ID: $USER_ID"
echo ""

# Test 5: Get the created user
echo "5️⃣ Testing Get User by ID..."
curl -s http://localhost:8000/api/v1/users/$USER_ID | jq
echo ""

# Test 6: Update the user
echo "6️⃣ Testing Update User..."
curl -s -X PUT http://localhost:8000/api/v1/users/$USER_ID \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Smith",
    "age": 31
  }' | jq
echo ""

# Test 7: Get all users again
echo "7️⃣ Testing Get All Users (after update)..."
curl -s http://localhost:8000/api/v1/users | jq
echo ""

# Test 8: Delete the user
echo "8️⃣ Testing Delete User..."
curl -s -X DELETE http://localhost:8000/api/v1/users/$USER_ID | jq
echo ""

# Test 9: Verify user is deleted
echo "9️⃣ Testing Get All Users (after deletion)..."
curl -s http://localhost:8000/api/v1/users | jq
echo ""

echo "✅ All API tests completed!"
echo ""
echo "🌐 Frontend is available at: http://localhost:3000"
echo "📚 API Documentation: http://localhost:8000/docs"
