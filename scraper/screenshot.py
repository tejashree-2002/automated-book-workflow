
# === scraper/screenshot.py ===

import asyncio
from playwright.async_api import async_playwright
import os

async def capture_screenshot_async(url, save_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=30000)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            await page.screenshot(path=save_path, full_page=True)
            print(f"✅ Screenshot saved at: {save_path}")
        except Exception as e:
            print("[Screenshot Error]", e)
        finally:
            await browser.close()

def capture_screenshot(url, path="screenshots/chapter1.png"):
    print("\n>> Taking screenshot of the chapter page...")
    asyncio.run(capture_screenshot_async(url, path))
