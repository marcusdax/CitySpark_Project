# 🏫 CitySpark Schools Setup Guide

## 🚀 Quick Start

### **1. Create Virtual Environment**
```batch
cd cityspark-schools
python -m venv venv
```

### **2. Activate Virtual Environment**
```batch
REM Windows
venv\Scripts\activate

REM Linux/Mac
source venv/bin/activate
```

### **3. Install Dependencies (Simplified)**
```batch
pip install fastapi uvicorn python-dotenv pydantic
pip install transformers torch scikit-learn
pip install github3.py requests beautifulsoup4
```

## 🛠️ Alternative Installation Methods

### **Method A: Minimal Installation (Recommended for Testing)**
```batch
pip install fastapi uvicorn python-dotenv pydantic
```

### **Method B: Install Without Database Dependencies**
```batch
pip install fastapi uvicorn python-dotenv pydantic transformers
```

### **Method C: Use Requirements.txt with Modifications**
```batch
REM Edit requirements.txt and remove psycopg2-binary and sqlalchemy
REM Then run:
pip install -r requirements.txt
```

## 📋 Troubleshooting

### **PostgreSQL Dependency Issue**
If you see `pg_config executable not found`:
```
1. Install PostgreSQL from https://www.postgresql.org/
2. Add PostgreSQL to your PATH
3. Or use sqlite instead (remove psycopg2-binary from requirements.txt)
```

### **Slow Installation**
The transformers and torch packages are large. If installation is slow:
```
1. Install minimal packages first
2. Test the application
3. Add AI packages later
```

### **Alternative: Use Pre-built Packages**
```batch
REM Install from pre-built wheels
pip install --prefer-binary fastapi uvicorn python-dotenv pydantic
```

## 🎯 Configuration

### **1. Copy Environment Template**
```batch
copy .env.example .env
```

### **2. Edit Configuration**
```batch
REM Edit .env file with your settings
notepad .env
```

### **3. Essential Configuration**
```env
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=True

# For testing, you can use these minimal settings
AI_HUB_API_URL=https://ai-hub.example.com/api
AI_HUB_API_KEY=test-key
GITHUB_API_TOKEN=your-github-token
```

## 🚀 Running the Application

### **1. Start FastAPI Server**
```batch
python main.py
```

### **2. Access API Documentation**
```
http://localhost:8000/api/docs
```

### **3. Test Health Endpoint**
```batch
curl http://localhost:8000/api/health
```

## 📚 Testing Without Full Dependencies

### **Test Core Functionality**
```python
from core.ai_learning.engine import CitySparkLearningEngine

# Initialize engine (will work without AI models)
engine = CitySparkLearningEngine()

# Test student registration
engine.register_student({
    "student_id": "test1",
    "name": "Test Student",
    "age": 18,
    "grade_level": "12"
})

print("✅ Core functionality working!")
```

## 🛡️ Minimal Setup for Development

### **1. Install Only Essential Packages**
```batch
pip install fastapi uvicorn python-dotenv pydantic
```

### **2. Run with Minimal Configuration**
```batch
python main.py
```

### **3. Test API Endpoints**
```batch
# Test health
curl http://localhost:8000/api/health

# Register student
curl -X POST http://localhost:8000/api/learning/register \
  -H "Content-Type: application/json" \
  -d '{"student_id": "test1", "name": "Test", "age": 18, "grade_level": "12"}'
```

## 🎯 Production Deployment

### **1. Install All Dependencies**
```batch
pip install -r requirements.txt
```

### **2. Configure for Production**
```env
DEBUG=False
APP_HOST=0.0.0.0
APP_PORT=8000
```

### **3. Run with Gunicorn**
```batch
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## 📋 Common Issues and Solutions

### **Issue: pip install is slow**
**Solution:** Install packages individually or use `--prefer-binary`

### **Issue: PostgreSQL dependency missing**
**Solution:** Remove psycopg2-binary from requirements.txt or install PostgreSQL

### **Issue: Memory errors during installation**
**Solution:** Install packages one at a time, starting with smaller ones

### **Issue: Python version compatibility**
**Solution:** Use Python 3.12+ as specified in requirements

## 🛠️ Manual Installation

### **Install Packages Individually**
```batch
pip install fastapi
pip install uvicorn
pip install python-dotenv
pip install pydantic
pip install transformers
pip install torch
pip install scikit-learn
pip install github3.py
pip install requests
pip install beautifulsoup4
```

### **Verify Installation**
```batch
python -c "import fastapi; print('FastAPI:', fastapi.__version__)"
python -c "import uvicorn; print('Uvicorn:', uvicorn.__version__)"
```

## 📚 Development Workflow

### **1. Activate Environment**
```batch
venv\Scripts\activate
```

### **2. Install/Update Packages**
```batch
pip install package-name
pip install --upgrade package-name
```

### **3. Run Application**
```batch
python main.py
```

### **4. Test Changes**
```batch
# Run tests
python -m pytest tests/

# Check API
curl http://localhost:8000/api/health
```

## 🎉 Success Criteria

### **Minimal Setup Working**
```
✅ Virtual environment created
✅ Essential packages installed
✅ Application starts without errors
✅ Health endpoint responds
```

### **Full Setup Working**
```
✅ All dependencies installed
✅ AI models loaded
✅ All API endpoints functional
✅ Database connection working (if configured)
```

## 📞 Need Help?

### **Common Commands**
```batch
REM List installed packages
pip list

REM Check Python version
python --version

REM Check pip version
pip --version

REM Upgrade pip
python -m pip install --upgrade pip
```

### **Debugging**
```batch
REM Check environment
python -c "import sys; print(sys.path)"

REM Test imports
python -c "import fastapi; import uvicorn"

REM Check virtual environment
where python
```

## 🎊 Next Steps

Once your environment is set up:
```
1. Test the API endpoints
2. Register a student
3. Generate a learning path
4. Explore the interactive features
5. Integrate with Omniscient Core AI Hub
```

**Let me know if you encounter any specific issues and I can provide targeted solutions!** 🚀