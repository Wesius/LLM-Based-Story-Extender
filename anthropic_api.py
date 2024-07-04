import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
API_URL = "https://api.anthropic.com/v1/messages"

async def process_with_claude(prompt):
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    data = {
        "model": "claude-3-5-sonnet-20240620",
        "max_tokens": 2048,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                return result['content'][0]['text']
            else:
                print(f"Error: {response.status}")
                print(await response.text())
                return None

async def generate_chapter_claude(prompt):
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
    }
    data = {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 4000,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                return result['content'][0]['text']
            else:
                print(f"Error: {response.status}")
                print(await response.text())
                return None

async def generate_chapter_plan(prompt):
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
    }
    data = {
        "model": "claude-3-5-sonnet-20240620",
        "max_tokens": 4000,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                return result['content'][0]['text']
            else:
                print(f"Error: {response.status}")
                print(await response.text())
                return None