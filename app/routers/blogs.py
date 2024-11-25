from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.blogs import Blog, BlogResponse
from app.services.blogs import BlogService

router = APIRouter()

@router.post("/", response_model=BlogResponse, status_code=201)
async def create_blog(blog: Blog):
    return await BlogService.create_blog(blog)

@router.get("/", response_model=List[BlogResponse])
async def get_blogs():
    return await BlogService.get_blogs()

@router.get("/{blog_id}", response_model=BlogResponse)
async def get_blog(blog_id: str):
    return await BlogService.get_blog(blog_id)

@router.put("/{blog_id}", response_model=BlogResponse)
async def update_blog(blog_id: str, blog: Blog):
    return await BlogService.update_blog(blog_id, blog)

@router.delete("/{blog_id}")
async def delete_blog(blog_id: str):
    return await BlogService.delete_blog(blog_id)
