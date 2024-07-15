import os
from crewai import Crew
from tasks.scraping_task import scraping_task
from tasks.pose_estimation_task import pose_estimation_task
from tasks.music_analysis_task import music_analysis_task
from tasks.choreography_task import choreography_task
from tasks.pose_mapping_task import pose_mapping_task
from agents.video_scraper import video_scraper
from agents.pose_estimator import pose_estimator
from agents.music_analysis import music_analysis_agent
from agents.choreography import choreography_agent
from agents.pose_mapping_agent import pose_mapping_agent

# Set environment variables for API keys (if necessary)
os.environ["SERPER_API_KEY"] = "Your Serper Key"
os.environ["OPENAI_API_KEY"] = "Your OpenAI Key"

# Initialize the crew with agents and their respective tasks
crew = Crew(
    agents=[
        video_scraper,
        pose_estimator,
        music_analysis_agent,
        choreography_agent,
        pose_mapping_agent
    ],
    tasks=[
        scraping_task,
        pose_estimation_task,
        music_analysis_task,
        choreography_task,
        pose_mapping_task
    ],
    verbose=2
)

# Function to kickoff the crew
def kickoff_crew():
    crew.kickoff()

if __name__ == "__main__":
    kickoff_crew()
