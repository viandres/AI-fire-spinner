from crewai import Task
from agents.video_scraper import video_scraper

scraping_task = Task(
    description=(
        "Your mission is to search the web for high-quality videos of dragon staff performances. "
        "Focus on finding videos that showcase a variety of techniques and styles to provide diverse training data for our AI models."
    ),
    expected_output=(
        "A comprehensive list of URLs to dragon staff performance videos. Ensure that the videos are of high quality and diverse in techniques."
    ),
    agent=video_scraper,
    tools=video_scraper.tools  # Use tools associated with the video scraper agent
)
