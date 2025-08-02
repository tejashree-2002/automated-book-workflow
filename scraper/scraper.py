import asyncio
from playwright.async_api import async_playwright

async def scrape_chapter_content(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=30000)
            # Grab the main content text from the chapter page
            content = await page.inner_text("#mw-content-text")
            await browser.close()
            return content.strip()
        except Exception as e:
            await browser.close()
            print("[Scraper Error]", e)
            return ""

def scrape_chapter(url):
    print("\n>> Scraping chapter content...")
    return asyncio.run(scrape_chapter_content(url))
