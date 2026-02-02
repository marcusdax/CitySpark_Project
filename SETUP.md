# 🚀 CitySpark Complete - Setup & Installation Guide

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
- **Python 3.12+** - [Download Here](https://www.python.org/downloads/)
- **Node.js 18+** - [Download Here](https://nodejs.org/)
- **Git** - [Download Here](https://git-scm.com/)
- **Visual Studio Code** - [Download Here](https://code.visualstudio.com/)

### Optional (for full functionality)
- **PostgreSQL** - [Download Here](https://www.postgresql.org/download/)
- **Redis** - [Download Here](https://redis.io/download)
- **Docker** - [Download Here](https://www.docker.com/products/docker-desktop)

## 🛠️ Installation Steps

### 1. Clone/Setup Project
```bash
# Navigate to your G: drive
cd G:\

# If cloning from git (replace with actual repo URL)
git clone <repository-url> CitySpark_Project

# Or if using the created folder
# The project should already be in G:\CitySpark_Project
cd CitySpark_Project
```

### 2. Backend Setup (Python)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# On Linux/Mac:
# source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Install additional dependencies for Windows
pip install --upgrade pip setuptools wheel
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### 3. Frontend Setup (Node.js)

```bash
# Install Node.js dependencies
npm install

# Or if you prefer yarn
yarn install
```

### 4. Environment Configuration

```bash
# Copy environment template
copy .env.example .env

# Edit .env file with your settings
# You can use notepad or VS Code
notepad .env
```

**Required Environment Variables:**
```env
# Basic Settings
APP_NAME="CitySpark Complete Platform"
DEBUG=True
SECRET_KEY="your-super-secret-key-change-this"

# GitHub Integration (Optional)
GITHUB_API_TOKEN=your-github-token-here

# AI Features (Optional)
AI_HUB_API_KEY=your-ai-hub-key-here
```

### 5. Database Setup (Optional - Uses SQLite by default)

**For SQLite (Default):**
```bash
# No setup required - database will be created automatically
```

**For PostgreSQL:**
```bash
# Install PostgreSQL
# Create database
createdb cityspark

# Update .env file
DATABASE_URL="postgresql://username:password@localhost/cityspark"
```

## 🚀 Running the Application

### Method 1: Development Mode

**Backend:**
```bash
# Activate virtual environment
venv\Scripts\activate

# Run the application
python main.py
```

**Frontend (Separate Terminal):**
```bash
# In a new terminal, navigate to project
cd G:\CitySpark_Project

# Start frontend development server
npm run dev
```

### Method 2: Simple Mode (Minimal Dependencies)

If you encounter dependency issues, run in simple mode:

```bash
# This will start a basic version without heavy ML dependencies
python main.py
```

### Method 3: Test Mode

```bash
# Run tests to verify installation
pytest tests/

# Or run specific test
python -m pytest tests/test_api.py -v
```

## 🌐 Accessing the Application

Once running, access the application at:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/health

## 🎯 Quick Test Commands

### Test Backend API
```bash
# Test health endpoint
curl http://localhost:8000/api/health

# Test learning endpoint
curl http://localhost:8000/api/learning/courses

# Test art generation
curl -X POST http://localhost:8000/api/art/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "modern city skyline", "style": "modern"}'
```

### Test Frontend
```bash
# Check if frontend is running
curl http://localhost:3000
```

## 🔧 Troubleshooting

### Common Issues

**1. Python Virtual Environment Issues:**
```bash
# Delete and recreate venv
rmdir /s venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**2. Port Already in Use:**
```bash
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F

# Or use different port in .env
PORT=8001
```

**3. Node.js Dependencies Issues:**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rmdir /s node_modules
del package-lock.json
npm install
```

**4. Database Connection Issues:**
```bash
# For SQLite, ensure write permissions
# For PostgreSQL, check connection string in .env

# Reset database (Caution: Deletes all data)
del cityspark.db
```

**5. Firewall Issues:**
```bash
# Add firewall rule for Python
netsh advfirewall firewall add rule name="CitySpark" dir=in action=allow protocol=TCP localport=8000,3000
```

### Performance Optimization

**For Better Performance:**
```bash
# Install GPU support (if you have NVIDIA GPU)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Enable Redis caching
# Install Redis and update REDIS_URL in .env

# Use PostgreSQL instead of SQLite for production
```

## 📚 Development Workflow

### Running Tests
```bash
# Backend tests
pytest tests/ -v

# Frontend tests
npm test

# Coverage report
pytest --cov=core tests/
```

### Code Quality
```bash
# Python formatting
black .
black --check .

# Linting
flake8 .

# Frontend linting
npm run lint
npm run type-check
```

### Database Migrations (if using PostgreSQL)
```bash
# Generate migration
alembic revision --autogenerate -m "描述更改"

# Apply migration
alembic upgrade head
```

## 🌍 Production Deployment

### Docker Deployment
```bash
# Build Docker image
docker build -t cityspark .

# Run container
docker run -p 8000:8000 --env-file .env cityspark
```

### Environment-Specific Configs

**Development (.env.development):**
```env
DEBUG=True
LOG_LEVEL=DEBUG
RELOAD=True
```

**Production (.env.production):**
```env
DEBUG=False
LOG_LEVEL=INFO
RELOAD=False
SECRET_KEY="production-secret-key"
```

## 📞 Getting Help

### Resources
- **Documentation**: Check the `/docs` folder
- **API Reference**: http://localhost:8000/docs
- **Issue Tracking**: Use the project's GitHub Issues

### Community Support
- **Discord**: [Community Server Link]
- **Stack Overflow**: Use tags `[cityspark]`
- **Email**: support@cityspark.org

---

## ✅ Verification Checklist

After installation, verify:

- [ ] Backend API responds at http://localhost:8000
- [ ] Frontend loads at http://localhost:3000
- [ ] API docs accessible at http://localhost:8000/docs
- [ ] Database connection working
- [ ] All tests pass: `pytest tests/`
- [ ] Frontend builds: `npm run build`

🎉 **Your CitySpark Complete Platform is now ready!**