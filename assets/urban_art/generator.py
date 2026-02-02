"""
🎨 CitySpark Urban Art Generator
AI-powered urban art creation and gallery management
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import json
from pathlib import Path

logger = logging.getLogger(__name__)


class UrbanArtGenerator:
    """AI-powered Urban Art Generator for CitySpark Platform"""

    def __init__(self):
        """Initialize the Urban Art Generator"""
        self.art_gallery = {}
        self.generation_history = []
        self.style_presets = self._load_style_presets()
        logger.info("🎨 Urban Art Generator initialized")

    def generate_art(
        self, prompt: str, style: str = "modern", user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate urban art based on prompt and style"""
        generation_id = f"art_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Simulate art generation (in real implementation, this would call AI models)
        art_piece = {
            "id": generation_id,
            "prompt": prompt,
            "style": style,
            "user_id": user_id,
            "title": self._generate_title(prompt, style),
            "description": self._generate_description(prompt, style),
            "metadata": self._generate_metadata(prompt, style),
            "image_url": f"/static/generated_art/{generation_id}.jpg",
            "thumbnail_url": f"/static/generated_art/{generation_id}_thumb.jpg",
            "tags": self._generate_tags(prompt, style),
            "created_at": datetime.now(),
            "likes": 0,
            "views": 0,
            "featured": False,
        }

        # Store in gallery
        self.art_gallery[generation_id] = art_piece
        self.generation_history.append(generation_id)

        logger.info(f"🎨 Generated urban art: {art_piece['title']} for user {user_id}")
        return art_piece

    def get_gallery(
        self, filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Get art gallery with optional filters"""
        gallery = list(self.art_gallery.values())

        if filters:
            # Apply filters
            if "style" in filters:
                gallery = [art for art in gallery if art["style"] == filters["style"]]

            if "user_id" in filters:
                gallery = [
                    art for art in gallery if art["user_id"] == filters["user_id"]
                ]

            if "tags" in filters:
                for tag in filters["tags"]:
                    gallery = [art for art in gallery if tag in art["tags"]]

            if "featured" in filters:
                gallery = [
                    art for art in gallery if art["featured"] == filters["featured"]
                ]

        # Sort by creation date (newest first)
        gallery.sort(key=lambda x: x["created_at"], reverse=True)

        return gallery

    def get_art_piece(self, art_id: str) -> Optional[Dict[str, Any]]:
        """Get specific art piece by ID"""
        return self.art_gallery.get(art_id)

    def update_art_piece(
        self, art_id: str, updates: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """Update art piece metadata"""
        if art_id not in self.art_gallery:
            return None

        art_piece = self.art_gallery[art_id]
        art_piece.update(updates)
        art_piece["updated_at"] = datetime.now()

        logger.info(f"📝 Updated art piece: {art_id}")
        return art_piece

    def like_art(self, art_id: str, user_id: str) -> Dict[str, Any]:
        """Like an art piece"""
        if art_id not in self.art_gallery:
            raise ValueError(f"Art piece {art_id} not found")

        art_piece = self.art_gallery[art_id]
        art_piece["likes"] += 1
        art_piece["updated_at"] = datetime.now()

        logger.info(f"❤️ User {user_id} liked art piece: {art_id}")
        return art_piece

    def view_art(self, art_id: str, user_id: str) -> Dict[str, Any]:
        """Record art piece view"""
        if art_id not in self.art_gallery:
            raise ValueError(f"Art piece {art_id} not found")

        art_piece = self.art_gallery[art_id]
        art_piece["views"] += 1

        logger.info(f"👁️ User {user_id} viewed art piece: {art_id}")
        return art_piece

    def feature_art(
        self, art_id: str, featured: bool = True
    ) -> Optional[Dict[str, Any]]:
        """Feature or unfeature an art piece"""
        if art_id not in self.art_gallery:
            return None

        art_piece = self.art_gallery[art_id]
        art_piece["featured"] = featured
        art_piece["updated_at"] = datetime.now()

        logger.info(f"⭐ Art piece {art_id} featured: {featured}")
        return art_piece

    def get_popular_art(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get most popular art pieces by likes and views"""
        gallery = list(self.art_gallery.values())

        # Calculate popularity score (likes * 2 + views * 0.1)
        for art in gallery:
            art["popularity_score"] = (art["likes"] * 2) + (art["views"] * 0.1)

        # Sort by popularity
        gallery.sort(key=lambda x: x["popularity_score"], reverse=True)

        return gallery[:limit]

    def get_style_suggestions(self, prompt: str) -> List[str]:
        """Get style suggestions based on prompt"""
        prompt_lower = prompt.lower()
        suggestions = []

        # Keyword-based style matching
        if any(word in prompt_lower for word in ["city", "urban", "street"]):
            suggestions.extend(["street_art", "graffiti", "urban"])

        if any(word in prompt_lower for word in ["modern", "contemporary", "abstract"]):
            suggestions.extend(["modern", "abstract", "contemporary"])

        if any(word in prompt_lower for word in ["nature", "green", "eco"]):
            suggestions.extend(["eco_art", "nature_inspired", "sustainable"])

        if any(word in prompt_lower for word in ["tech", "digital", "cyber"]):
            suggestions.extend(["digital", "cyberpunk", "tech_art"])

        # Add default suggestions if none matched
        if not suggestions:
            suggestions = ["modern", "abstract", "contemporary"]

        return list(set(suggestions))  # Remove duplicates

    def create_collection(
        self, name: str, description: str, art_ids: List[str], user_id: str
    ) -> Dict[str, Any]:
        """Create an art collection"""
        collection_id = f"collection_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Verify all art pieces exist
        valid_art_ids = [art_id for art_id in art_ids if art_id in self.art_gallery]

        collection = {
            "id": collection_id,
            "name": name,
            "description": description,
            "art_ids": valid_art_ids,
            "user_id": user_id,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
            "public": False,
            "likes": 0,
            "views": 0,
        }

        # Save collection (in real implementation, use database)
        collections_path = Path("assets/urban_art/collections.json")
        collections = []

        if collections_path.exists():
            with open(collections_path, "r") as f:
                collections = json.load(f)

        collections.append(collection)

        # Save collections
        collections_path.parent.mkdir(parents=True, exist_ok=True)
        with open(collections_path, "w") as f:
            json.dump(collections, f, indent=2, default=str)

        logger.info(
            f"📚 Created collection: {name} with {len(valid_art_ids)} art pieces"
        )
        return collection

    def _load_style_presets(self) -> Dict[str, Dict[str, Any]]:
        """Load style presets for art generation"""
        return {
            "modern": {
                "name": "Modern Urban",
                "description": "Contemporary urban art with clean lines and bold colors",
                "color_palette": [
                    "#FF6B6B",
                    "#4ECDC4",
                    "#45B7D1",
                    "#96CEB4",
                    "#FFEAA7",
                ],
                "techniques": ["digital", "mixed_media", "collage"],
            },
            "graffiti": {
                "name": "Graffiti Style",
                "description": "Classic street art with spray paint techniques",
                "color_palette": [
                    "#FF0000",
                    "#FFD700",
                    "#00FF00",
                    "#FF00FF",
                    "#00FFFF",
                ],
                "techniques": ["spray_paint", "stencil", "freehand"],
            },
            "abstract": {
                "name": "Abstract Urban",
                "description": "Abstract interpretation of urban landscapes",
                "color_palette": [
                    "#2C3E50",
                    "#E74C3C",
                    "#F39C12",
                    "#27AE60",
                    "#8E44AD",
                ],
                "techniques": ["geometric", "expressionist", "minimalist"],
            },
            "eco_art": {
                "name": "Eco Urban Art",
                "description": "Environmentally conscious urban art themes",
                "color_palette": [
                    "#27AE60",
                    "#16A085",
                    "#2980B9",
                    "#8E44AD",
                    "#F39C12",
                ],
                "techniques": ["recycled_materials", "natural_elements", "sustainable"],
            },
        }

    def _generate_title(self, prompt: str, style: str) -> str:
        """Generate a title for the art piece"""
        style_info = self.style_presets.get(style, {})
        style_name = style_info.get("name", style.capitalize())

        # Simple title generation (in real implementation, use AI)
        title_words = prompt.split()[:3]  # Take first 3 words
        title = " ".join(title_words).title()

        return f"{title} - {style_name} Style"

    def _generate_description(self, prompt: str, style: str) -> str:
        """Generate description for the art piece"""
        style_info = self.style_presets.get(style, {})
        style_desc = style_info.get("description", "")

        return f"AI-generated urban art inspired by: {prompt}. {style_desc}"

    def _generate_metadata(self, prompt: str, style: str) -> Dict[str, Any]:
        """Generate metadata for the art piece"""
        return {
            "prompt_length": len(prompt),
            "style": style,
            "generation_model": "CitySpark-Art-v1.0",
            "resolution": "1920x1080",
            "format": "digital_art",
            "keywords": self._generate_tags(prompt, style),
        }

    def _generate_tags(self, prompt: str, style: str) -> List[str]:
        """Generate tags for the art piece"""
        tags = [style]

        # Extract keywords from prompt
        prompt_words = prompt.lower().split()
        urban_keywords = [
            "city",
            "urban",
            "street",
            "building",
            "skyline",
            "modern",
            "contemporary",
        ]

        for word in prompt_words:
            if word in urban_keywords:
                tags.append(word)

        # Add style-specific tags
        if style == "graffiti":
            tags.extend(["street_art", "spray_paint", "wall_art"])
        elif style == "eco_art":
            tags.extend(["environment", "sustainable", "green"])
        elif style == "modern":
            tags.extend(["contemporary", "minimalist", "clean"])

        return list(set(tags))  # Remove duplicates
