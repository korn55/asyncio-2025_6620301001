import asyncio 
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/delay/3")
        print(response.status_code)
        print(response.text)[:100] # First 100 characters 

asyncio.run(main())