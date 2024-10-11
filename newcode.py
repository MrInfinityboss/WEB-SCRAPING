from playwright.sync_api import sync_playwright
import time

def scrape_profile(url: str) -> dict:
    """
    Scrape an X.com profile details e.g.: https://x.com/Scrapfly_dev
    """
    _xhr_calls = []

    def intercept_response(response):
        """Capture all background requests and save them"""
        # Capture all network responses (not just XHR)
        _xhr_calls.append(response)
        print(f"Response URL: {response.url}")  # Log the URL of every response
        try:
            print(f"Response JSON: {response.json()}")  # Try to log JSON content if it's available
        except Exception as e:
            print(f"Non-JSON response: {e}")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # Enable background request intercepting
        page.on("response", intercept_response)
        
        # Go to URL and wait for the page to load
        page.goto(url)
        page.wait_for_selector("[data-testid='primaryColumn']")

        # Give extra time for XHR requests to fire
        print("Waiting for additional XHR requests...")
        time.sleep(10)  # You may increase this value to ensure the XHR requests happen

        # Log all captured XHR requests
        if not _xhr_calls:
            print("No network calls captured.")
        else:
            print(f"Total captured responses: {len(_xhr_calls)}")
        
        # Check for relevant XHR requests containing "UserBy"
        tweet_calls = [f for f in _xhr_calls if "UserBy" in f.url]
        if not tweet_calls:
            print("No XHR calls with 'UserBy' found.")
        else:
            for xhr in tweet_calls:
                data = xhr.json()
                return data['data']['user']['result']

    return None


if __name__ == "__main__":
    profile_data = scrape_profile("https://x.com/Scrapfly_dev")
    if profile_data:
        print(profile_data)
    else:
        print("No profile data found.")
