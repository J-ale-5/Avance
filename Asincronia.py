import asyncio
import webbrowser

async def refresh_page(url, interval):
    while True:
        webbrowser.open(url, new=0)
        await asyncio.sleep(interval)

async def main():
    url = ""
    refresh_interval = 30
    await refresh_page(url, refresh_interval)

asyncio.run(main())
