# 🏫 CitySpark Schools Quick Start Guide

## ✅ Current Status

### **What's Working**
```
✅ Virtual environment created
✅ Core packages installed (fastapi, uvicorn, pydantic, python-dotenv)
✅ Project structure complete
✅ API endpoints ready
✅ Configuration files prepared
```

### **What You Can Do Now**
```
✅ Run the FastAPI server
✅ Test API endpoints
✅ Register students
✅ Generate learning paths (basic functionality)
✅ Track progress
✅ Get recommendations
```

## 🚀 Run the Application

### **1. Start the Server**
```batch
cd cityspark-schools
venv\Scripts\activate
python main.py
```

### **2. Access the API**
```
http://localhost:8000/api/docs
```

### **3. Test Endpoints**
```batch
# Test health
curl http://localhost:8000/api/health

# Register a student
curl -X POST http://localhost:8000/api/learning/register \
  -H "Content-Type: application/json" \
  -d '{"student_id": "student1", "name": "John Doe", "age": 18, "grade_level": "12"}'

# Generate learning path
curl -X POST http://localhost:8000/api/learning/path \
  -H "Content-Type: application/json" \
  -d '{"student_id": "student1", "curriculum": "computer_science_101"}'
```

## 🛠️ What's Missing (Optional)

### **AI Packages (Can be Added Later)**
```
- transformers (for AI models)
- torch (for deep learning)
- scikit-learn (for ML algorithms)
- github3.py (for GitHub integration)
```

### **Database (Can be Added Later)**
```
- psycopg2-binary (PostgreSQL)
- sqlalchemy (ORM)
```

## 🎯 What You Can Test Now

### **Core Functionality**
```python
from core.ai_learning.engine import CitySparkLearningEngine

# Initialize engine
engine = CitySparkLearningEngine()

# Register student
engine.register_student({
    "student_id": "test1",
    "name": "Test Student",
    "age": 18,
    "grade_level": "12"
})

# Generate learning path
learning_path = engine.generate_learning_path("test1", "computer_science_101")

print("✅ Core functionality working!")
print(f"Generated path: {learning_path.path_id}")
```

## 📚 API Endpoints Available

### **Learning Engine**
```
POST /api/learning/register       # Register student
POST /api/learning/path          # Generate learning path
POST /api/learning/track         # Track progress
GET /api/learning/recommendations # Get recommendations
GET /api/learning/patterns        # Analyze patterns
GET /api/learning/progress        # Get progress
GET /api/learning/students        # List students
GET /api/learning/curricula       # List curricula
```

## 🛡️ Minimal Configuration

### **.env File**
```env
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=True

# For testing, use these minimal settings
AI_HUB_API_URL=https://ai-hub.example.com/api
AI_HUB_API_KEY=test-key
GITHUB_API_TOKEN=your-github-token
```

## 🎉 Next Steps

### **Option 1: Test Current Functionality**
```
1. Run the server: python main.py
2. Test API endpoints
3. Explore core features
```

### **Option 2: Add AI Packages Later**
```batch
pip install transformers torch scikit-learn
```

### **Option 3: Add Database Later**
```batch
pip install psycopg2-binary sqlalchemy
```

## 📋 Troubleshooting

### **If You Get Errors**
```
1. Check virtual environment is activated
2. Verify packages are installed
3. Check Python version (3.12+ required)
4. Review error messages
```

### **Common Fixes**
```batch
REM Reinstall packages
pip install --force-reinstall fastapi uvicorn

REM Check Python path
where python

REM Verify virtual environment
venv\Scripts\python --version
```

## 🎊 Success Criteria

### **Minimal Setup Working**
```
✅ Server starts without errors
✅ Health endpoint responds
✅ Student registration works
✅ Learning path generation works
✅ Progress tracking works
```

### **Full Setup Working**
```
✅ All packages installed
✅ AI models loaded
✅ All API endpoints functional
✅ Database connection working
```

## 📞 Need Help?

**Common Issues:**
- Virtual environment not activated
- Package installation failures
- Python version mismatch
- Missing dependencies

**Solutions:**
1. Activate virtual environment
2. Install packages individually
3. Check Python version
4. Review error messages

**Let me know what specific issues you encounter and I can help!** 🚀