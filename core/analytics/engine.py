# 📈 CitySpark Analytics Engine
# Learning analytics and data insights

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import json


class AnalyticsEngine:
    """Handles learning analytics and data insights"""

    def __init__(self):
        self.events = []
        self.metrics = {}
        self.aggregated_data = {}

    def track_event(
        self, event_type: str, user_id: str, data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Track a learning event"""
        event = {
            "id": f"event_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
            "type": event_type,
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
            "data": data,
        }

        self.events.append(event)
        return event

    def calculate_user_metrics(self, user_id: str, days: int = 30) -> Dict[str, Any]:
        """Calculate metrics for a user over specified days"""
        cutoff_date = datetime.now() - timedelta(days=days)
        user_events = [
            e
            for e in self.events
            if e["user_id"] == user_id
            and datetime.fromisoformat(e["timestamp"]) >= cutoff_date
        ]

        return {
            "user_id": user_id,
            "period_days": days,
            "total_events": len(user_events),
            "learning_time_minutes": self._calculate_learning_time(user_events),
            "completion_rate": self._calculate_completion_rate(user_events),
            "average_score": self._calculate_average_score(user_events),
            "engagement_score": self._calculate_engagement_score(user_events),
        }

    def generate_insights(self, user_id: str) -> List[Dict[str, Any]]:
        """Generate learning insights for a user"""
        user_events = [e for e in self.events if e["user_id"] == user_id]

        insights = []

        # Learning patterns
        if self._is_night_learner(user_events):
            insights.append(
                {
                    "type": "learning_pattern",
                    "title": "Night Learner",
                    "description": "You learn most effectively during evening hours",
                    "recommendation": "Schedule important learning activities for 7-10 PM",
                }
            )

        # Progress trends
        if self._is_improving(user_events):
            insights.append(
                {
                    "type": "progress_trend",
                    "title": "Improving Performance",
                    "description": "Your scores have been trending upward",
                    "recommendation": "Keep up the current learning strategy",
                }
            )

        return insights

    def _calculate_learning_time(self, events: List[Dict[str, Any]]) -> int:
        """Calculate total learning time in minutes"""
        learning_events = [
            e
            for e in events
            if e["type"] in ["learning_session", "video_watch", "quiz_attempt"]
        ]
        total_time = sum(
            e.get("data", {}).get("duration_minutes", 0) for e in learning_events
        )
        return total_time

    def _calculate_completion_rate(self, events: List[Dict[str, Any]]) -> float:
        """Calculate completion rate"""
        started_events = [e for e in events if e["type"] == "module_started"]
        completed_events = [e for e in events if e["type"] == "module_completed"]

        return (
            (len(completed_events) / len(started_events)) * 100 if started_events else 0
        )

    def _calculate_average_score(self, events: List[Dict[str, Any]]) -> float:
        """Calculate average score from quiz attempts"""
        quiz_events = [e for e in events if e["type"] == "quiz_completed"]
        scores = [e.get("data", {}).get("score", 0) for e in quiz_events]

        return sum(scores) / len(scores) if scores else 0

    def _calculate_engagement_score(self, events: List[Dict[str, Any]]) -> float:
        """Calculate engagement score"""
        engagement_events = [
            "video_watch",
            "quiz_attempt",
            "discussion_post",
            "assignment_submit",
        ]
        relevant_events = [e for e in events if e["type"] in engagement_events]

        # Simple engagement scoring
        return min(len(relevant_events) * 5, 100)

    def _is_night_learner(self, events: List[Dict[str, Any]]) -> bool:
        """Check if user learns primarily at night"""
        learning_events = [
            e for e in events if e["type"] in ["learning_session", "video_watch"]
        ]
        if not learning_events:
            return False

        evening_hours = [19, 20, 21, 22, 23]  # 7 PM - 11 PM
        evening_events = 0

        for event in learning_events:
            hour = datetime.fromisoformat(event["timestamp"]).hour
            if hour in evening_hours:
                evening_events += 1

        return evening_events / len(learning_events) > 0.6

    def _is_improving(self, events: List[Dict[str, Any]]) -> bool:
        """Check if user's performance is improving"""
        quiz_events = [e for e in events if e["type"] == "quiz_completed"]
        if len(quiz_events) < 3:
            return False

        quiz_events.sort(key=lambda x: x["timestamp"])
        recent_scores = [e.get("data", {}).get("score", 0) for e in quiz_events[-3:]]
        early_scores = [e.get("data", {}).get("score", 0) for e in quiz_events[:3]]

        return sum(recent_scores) / len(recent_scores) > sum(early_scores) / len(
            early_scores
        )
