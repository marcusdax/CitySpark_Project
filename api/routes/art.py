"""
🎨 CitySpark Urban Art API Routes
Endpoints for urban art generation, gallery, and collections
"""

from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


# Pydantic models
class ArtGenerationRequest(BaseModel):
    prompt: str
    style: str = "modern"
    user_id: Optional[str] = None


class ArtUpdateRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None


class CollectionCreateRequest(BaseModel):
    name: str
    description: str
    art_ids: List[str]
    user_id: str
    public: bool = False


# Mock art generator (in real implementation, inject dependency)
from assets.urban_art.generator import UrbanArtGenerator

art_generator = UrbanArtGenerator()


@router.post("/generate")
async def generate_art(request: ArtGenerationRequest):
    """Generate urban art based on prompt and style"""
    try:
        art_piece = art_generator.generate_art(
            request.prompt, request.style, request.user_id
        )
        return {"message": "Art generated successfully", "art_piece": art_piece}
    except Exception as e:
        logger.error(f"Error generating art: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/gallery")
async def get_art_gallery(
    style: Optional[str] = None,
    user_id: Optional[str] = None,
    tags: Optional[List[str]] = None,
    featured: Optional[bool] = None,
    limit: int = 50,
):
    """Get art gallery with filters"""
    try:
        filters = {}
        if style:
            filters["style"] = style
        if user_id:
            filters["user_id"] = user_id
        if tags:
            filters["tags"] = tags
        if featured is not None:
            filters["featured"] = featured

        gallery = art_generator.get_gallery(filters)

        # Apply limit
        if limit > 0:
            gallery = gallery[:limit]

        return {
            "gallery": gallery,
            "total_count": len(gallery),
            "filters_applied": filters,
        }
    except Exception as e:
        logger.error(f"Error getting gallery: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/gallery/{art_id}")
async def get_art_piece(art_id: str):
    """Get specific art piece by ID"""
    try:
        art_piece = art_generator.get_art_piece(art_id)
        if not art_piece:
            raise HTTPException(status_code=404, detail="Art piece not found")

        return {"art_piece": art_piece}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting art piece: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/gallery/{art_id}")
async def update_art_piece(art_id: str, updates: ArtUpdateRequest):
    """Update art piece metadata"""
    try:
        art_piece = art_generator.update_art_piece(
            art_id, updates.dict(exclude_unset=True)
        )
        if not art_piece:
            raise HTTPException(status_code=404, detail="Art piece not found")

        return {"message": "Art piece updated successfully", "art_piece": art_piece}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating art piece: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/gallery/{art_id}/like")
async def like_art_piece(art_id: str, user_id: str):
    """Like an art piece"""
    try:
        art_piece = art_generator.like_art(art_id, user_id)
        return {"message": "Art piece liked successfully", "art_piece": art_piece}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error liking art piece: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/gallery/{art_id}/view")
async def view_art_piece(art_id: str, user_id: str):
    """Record art piece view"""
    try:
        art_piece = art_generator.view_art(art_id, user_id)
        return {"message": "View recorded successfully", "art_piece": art_piece}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Error viewing art piece: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/gallery/{art_id}/feature")
async def feature_art_piece(art_id: str, featured: bool = True):
    """Feature or unfeature an art piece"""
    try:
        art_piece = art_generator.feature_art(art_id, featured)
        if not art_piece:
            raise HTTPException(status_code=404, detail="Art piece not found")

        return {
            "message": f"Art piece {'featured' if featured else 'unfeatured'} successfully",
            "art_piece": art_piece,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error featuring art piece: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/popular")
async def get_popular_art(limit: int = 10):
    """Get most popular art pieces"""
    try:
        popular_art = art_generator.get_popular_art(limit)
        return {"popular_art": popular_art, "total_count": len(popular_art)}
    except Exception as e:
        logger.error(f"Error getting popular art: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/styles")
async def get_available_styles():
    """Get available art styles"""
    styles = {
        "modern": {
            "name": "Modern Urban",
            "description": "Contemporary urban art with clean lines and bold colors",
            "color_palette": ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"],
            "techniques": ["digital", "mixed_media", "collage"],
            "examples": [
                "Digital City Skyline",
                "Modern Architecture",
                "Abstract Urban",
            ],
        },
        "graffiti": {
            "name": "Graffiti Style",
            "description": "Classic street art with spray paint techniques",
            "color_palette": ["#FF0000", "#FFD700", "#00FF00", "#FF00FF", "#00FFFF"],
            "techniques": ["spray_paint", "stencil", "freehand"],
            "examples": ["Street Tags", "Mural Art", "Stencil Work"],
        },
        "abstract": {
            "name": "Abstract Urban",
            "description": "Abstract interpretation of urban landscapes",
            "color_palette": ["#2C3E50", "#E74C3C", "#F39C12", "#27AE60", "#8E44AD"],
            "techniques": ["geometric", "expressionist", "minimalist"],
            "examples": ["Geometric City", "Abstract Architecture", "Minimalist Urban"],
        },
        "eco_art": {
            "name": "Eco Urban Art",
            "description": "Environmentally conscious urban art themes",
            "color_palette": ["#27AE60", "#16A085", "#2980B9", "#8E44AD", "#F39C12"],
            "techniques": ["recycled_materials", "natural_elements", "sustainable"],
            "examples": ["Green City", "Sustainable Art", "Eco Urbanism"],
        },
    }

    return {"styles": styles}


@router.get("/styles/suggestions")
async def get_style_suggestions(prompt: str):
    """Get style suggestions based on prompt"""
    try:
        suggestions = art_generator.get_style_suggestions(prompt)
        return {
            "prompt": prompt,
            "suggestions": suggestions,
            "recommended": suggestions[0] if suggestions else "modern",
        }
    except Exception as e:
        logger.error(f"Error getting style suggestions: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/collections")
async def create_collection(request: CollectionCreateRequest):
    """Create an art collection"""
    try:
        collection = art_generator.create_collection(
            request.name, request.description, request.art_ids, request.user_id
        )
        return {"message": "Collection created successfully", "collection": collection}
    except Exception as e:
        logger.error(f"Error creating collection: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/collections")
async def get_collections(user_id: Optional[str] = None, public: Optional[bool] = None):
    """Get art collections"""
    # In real implementation, this would query database
    collections = [
        {
            "id": "collection_1",
            "name": "Modern Urban Art",
            "description": "Collection of contemporary urban artworks",
            "art_count": 15,
            "user_id": "user_123",
            "public": True,
            "likes": 125,
            "views": 890,
            "created_at": datetime.now().isoformat(),
        },
        {
            "id": "collection_2",
            "name": "Street Art Gallery",
            "description": "Best street art from around the world",
            "art_count": 23,
            "user_id": "user_456",
            "public": True,
            "likes": 210,
            "views": 1450,
            "created_at": datetime.now().isoformat(),
        },
    ]

    # Apply filters
    if user_id:
        collections = [c for c in collections if c["user_id"] == user_id]
    if public is not None:
        collections = [c for c in collections if c["public"] == public]

    return {"collections": collections, "total_count": len(collections)}


@router.get("/collections/{collection_id}")
async def get_collection_details(collection_id: str):
    """Get detailed information about a collection"""
    # Mock collection details
    collection = {
        "id": collection_id,
        "name": "Modern Urban Art",
        "description": "A curated collection of contemporary urban artworks featuring modern themes and techniques.",
        "art_pieces": [
            {
                "id": "art_1",
                "title": "Digital City Skyline",
                "artist": "AI Generator",
                "style": "modern",
                "image_url": "/static/art/art_1.jpg",
                "likes": 45,
            },
            {
                "id": "art_2",
                "title": "Urban Abstract",
                "artist": "AI Generator",
                "style": "abstract",
                "image_url": "/static/art/art_2.jpg",
                "likes": 32,
            },
        ],
        "user_id": "user_123",
        "public": True,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "tags": ["modern", "urban", "contemporary"],
        "likes": 125,
        "views": 890,
    }

    return {"collection": collection}


@router.post("/upload")
async def upload_artwork(
    file: UploadFile = File(...),
    title: str = None,
    description: str = None,
    tags: str = None,
    user_id: str = None,
):
    """Upload user-created artwork"""
    # In real implementation, this would save file and create database entry
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    uploaded_art = {
        "id": f"upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "title": title or file.filename,
        "description": description or "User uploaded artwork",
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size,
        "user_id": user_id,
        "tags": tags.split(",") if tags else [],
        "uploaded_at": datetime.now().isoformat(),
        "likes": 0,
        "views": 0,
    }

    return {"message": "Artwork uploaded successfully", "artwork": uploaded_art}


@router.get("/search")
async def search_artwork(
    q: str,
    style: Optional[str] = None,
    tags: Optional[List[str]] = None,
    limit: int = 20,
):
    """Search for artwork"""
    # In real implementation, this would search database
    results = []

    # Mock search results
    if q.lower() in ["city", "urban", "modern"]:
        results.extend(
            [
                {
                    "id": "art_1",
                    "title": "Digital City Skyline",
                    "description": "Modern urban skyline in digital style",
                    "style": "modern",
                    "tags": ["city", "digital", "skyline"],
                    "image_url": "/static/art/art_1.jpg",
                    "relevance_score": 0.95,
                }
            ]
        )

    return {
        "query": q,
        "results": results[:limit],
        "total_count": len(results),
        "search_time_ms": 25,
    }


@router.get("/stats")
async def get_art_statistics():
    """Get art gallery statistics"""
    return {
        "total_art_pieces": len(art_generator.art_gallery),
        "total_collections": 0,
        "total_views": sum(
            art.get("views", 0) for art in art_generator.art_gallery.values()
        ),
        "total_likes": sum(
            art.get("likes", 0) for art in art_generator.art_gallery.values()
        ),
        "style_distribution": {"modern": 0, "graffiti": 0, "abstract": 0, "eco_art": 0},
        "daily_generation": [
            {"date": "2024-01-19", "count": 0},
            {"date": "2024-01-18", "count": 0},
        ],
        "popular_tags": ["urban", "modern", "digital", "art", "creative"],
    }
