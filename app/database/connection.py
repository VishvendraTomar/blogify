from motor.motor_asyncio import AsyncIOMotorClient
import certifi

MONGODB_URI = "mongodb+srv://vishvendratomar29:homenopegone@fastapi0.iktdh.mongodb.net/?retryWrites=true&w=majority&appName=Fastapi0"

client = AsyncIOMotorClient(MONGODB_URI, tlsCAFile=certifi.where())
db = client.get_database("blogify")
