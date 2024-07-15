from crewai import Agent
from tools.selenium_scraper import SeleniumScraper

video_scraper = Agent(
    role="Video Scraper",
    goal="Collect dragon staff performance videos to provide raw data for AI training",
    backstory=(
        "You are responsible for scouring the internet to find high-quality videos of dragon staff performances. "
        "These videos are crucial for training our AI models to understand and replicate the complex movements "
        "involved in dragon staff firespinning. Ensure the videos are diverse and cover various techniques and styles."
    ),
    tools=[SeleniumScraper()],
    verbose=True,
    allow_delegation=True
)
