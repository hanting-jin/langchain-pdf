import os
import redis

client = redis.Redis.from_url(
    os.getenv["REDIS_URL"],
    decode_responses=True,
)