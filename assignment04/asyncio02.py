# Create 1 Task with High-Level API
import asyncio

async def do_something():
    print("เริ่มทํางาน...")
    await asyncio.sleep(2)
    print("ทํางานเสร็จแล้ว!")

async def main():
    task = asyncio.create_task(do_something())
    await task # รอให้ task เสร็จ

asyncio.run(main())