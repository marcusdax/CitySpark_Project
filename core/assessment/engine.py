# 📊 CitySpark Assessment System
# Student assessment and evaluation framework

from typing import Dict, List, Any, Optional
from datetime import datetime
import json


class AssessmentEngine:
    """Handles student assessments and evaluations"""

    def __init__(self):
        self.assessments = {}
        self.submissions = {}
        self.grading_criteria = {}

    def create_assessment(self, assessment_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new assessment"""
        assessment_id = assessment_data.get(
            "id", f"assessment_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )

        assessment = {
            "id": assessment_id,
            "title": assessment_data.get("title", ""),
            "type": assessment_data.get("type", "quiz"),
            "course_id": assessment_data.get("course_id", ""),
            "questions": assessment_data.get("questions", []),
            "time_limit": assessment_data.get("time_limit", 60),
            "max_score": assessment_data.get("max_score", 100),
            "passing_score": assessment_data.get("passing_score", 70),
            "created_at": datetime.now().isoformat(),
        }

        self.assessments[assessment_id] = assessment
        return assessment

    def evaluate_submission(
        self, assessment_id: str, student_id: str, submission: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Evaluate a student submission"""
        assessment = self.assessments.get(assessment_id)
        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        # Simple scoring logic (would be more sophisticated in production)
        score = self._calculate_score(submission, assessment)
        passed = score >= assessment["passing_score"]

        result = {
            "assessment_id": assessment_id,
            "student_id": student_id,
            "score": score,
            "max_score": assessment["max_score"],
            "passed": passed,
            "feedback": self._generate_feedback(score, assessment),
            "submitted_at": datetime.now().isoformat(),
        }

        self.submissions[f"{assessment_id}_{student_id}"] = result
        return result

    def _calculate_score(
        self, submission: Dict[str, Any], assessment: Dict[str, Any]
    ) -> float:
        """Calculate score for submission"""
        # Simplified scoring - in real implementation would be more complex
        answers = submission.get("answers", {})
        total_questions = len(assessment.get("questions", []))
        correct_answers = sum(
            1
            for q in assessment.get("questions", [])
            if answers.get(q.get("id")) == q.get("correct_answer")
        )

        return (
            (correct_answers / total_questions) * assessment["max_score"]
            if total_questions > 0
            else 0
        )

    def _generate_feedback(self, score: float, assessment: Dict[str, Any]) -> str:
        """Generate feedback based on score"""
        percentage = (score / assessment["max_score"]) * 100

        if percentage >= 90:
            return "Excellent work! You've mastered this material."
        elif percentage >= 80:
            return "Great job! You have a strong understanding of this topic."
        elif percentage >= 70:
            return "Good work! Review the areas where you lost points."
        else:
            return "You need to review this material more thoroughly."
