# 📚 CitySpark Curriculum Framework
# Educational content structure and management

from typing import Dict, List, Any, Optional
from datetime import datetime
import json


class CurriculumManager:
    """Manages educational curriculum and content"""

    def __init__(self):
        self.courses = {}
        self.subjects = {}
        self.learning_objectives = {}

    def create_course(self, course_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new course"""
        course_id = course_data.get(
            "id", f"course_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )

        course = {
            "id": course_id,
            "title": course_data.get("title", ""),
            "description": course_data.get("description", ""),
            "subject": course_data.get("subject", ""),
            "difficulty": course_data.get("difficulty", "beginner"),
            "duration": course_data.get("duration", 0),
            "modules": course_data.get("modules", []),
            "objectives": course_data.get("objectives", []),
            "prerequisites": course_data.get("prerequisites", []),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }

        self.courses[course_id] = course
        return course

    def get_course(self, course_id: str) -> Optional[Dict[str, Any]]:
        """Get course by ID"""
        return self.courses.get(course_id)

    def list_courses(
        self, subject: Optional[str] = None, difficulty: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List courses with optional filters"""
        courses = list(self.courses.values())

        if subject:
            courses = [c for c in courses if c.get("subject") == subject]

        if difficulty:
            courses = [c for c in courses if c.get("difficulty") == difficulty]

        return courses
