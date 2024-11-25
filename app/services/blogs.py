from app.database.blogs import posts_collection
from app.schemas.blogs import Blog, BlogResponse
from bson import ObjectId
from fastapi import HTTPException

class BlogService:
    @staticmethod
    async def create_blog(blog: Blog) -> BlogResponse:
        result = await posts_collection.insert_one(blog.dict())
        return BlogResponse(id=str(result.inserted_id), **blog.dict())

    @staticmethod
    async def get_blogs():
        blogs = await posts_collection.find().to_list(100)
        return [BlogResponse(id=str(blog["_id"]), **blog) for blog in blogs]

    @staticmethod
    async def get_blog(blog_id: str):
        blog = await posts_collection.find_one({"_id": ObjectId(blog_id)})
        if not blog:
            raise HTTPException(status_code=404, detail="Blog not found")
        return BlogResponse(id=str(blog["_id"]), **blog)

    @staticmethod
    async def update_blog(blog_id: str, blog: Blog):
        result = await posts_collection.update_one({"_id": ObjectId(blog_id)}, {"$set": blog.dict()})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Blog not found")
        updated_blog = await posts_collection.find_one({"_id": ObjectId(blog_id)})
        return BlogResponse(id=str(updated_blog["_id"]), **updated_blog)

    @staticmethod
    async def delete_blog(blog_id: str):
        result = await posts_collection.delete_one({"_id": ObjectId(blog_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Blog not found")
        return {"message": "Blog deleted successfully"}
